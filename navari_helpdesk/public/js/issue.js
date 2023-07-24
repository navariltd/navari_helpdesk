frappe.ui.form.on('Issue', {
    onload: function (frm) {
        cur_frm.dashboard.hide()

        if(frm.doc.status == 'Closed') {
	        frm.add_custom_button(__('Reopen Issue'), function(){
	            reopen_issue(frm)
	        });
	    }
	    
        cur_frm.set_query("issue_type", function () {
            return {
                "filters": {
                    "department": frm.doc.department
                }
            };
        });
    },
    department: function (frm) {
        if (frm.doc.department) {
            get_hod_details(frm);
            get_receivers_list(frm);
            frm.set_value('sms_sent', 0);
        }
    },
    validate: function (frm) {
        if(frm.doc.status == 'Closed') {
            if(frm.doc.raised_by != frappe.session.user){
                frappe.msgprint(`Cannot close issue since it was created by a different user: ${frm.doc.raised_by_name}`)
                throw new Error("Cannot close issue")
            }
        }

        if(frm.doc.status == 'Open') {
            reopen_issue(frm)
        }
    },
    after_save: function (frm) {
        if (frm.doc.status == 'Open' && !frm.doc.sms_sent){
            send_sms(frm);
            frm.set_value('sms_sent', 1);
            frm.save();
        }
    }
});

const get_hod_details = function (frm) {
    if (frm.doc.department) {
        frappe.model.with_doc('Department', frm.doc.department, function () {
            let dept = frappe.model.get_doc('Department', frm.doc.department);
            frm.set_value('hod', dept['hod']);
            refresh_field('hod');
            
            //Get employee user id
            if (frm.doc.hod){
                frappe.model.with_doc('Employee', frm.doc.hod, function () {
                    let emp = frappe.model.get_doc('Employee', frm.doc.hod);
                    frm.set_value('hod_user_id', emp['user_id']);
                    refresh_field('hod_user_id');
                });
            }
        });
    }
}

const send_sms = async function (frm) {
    let phone_number_list = await frappe.call({
        method: "navari_helpdesk.controllers.receiver_list_utils.strip_phone_numbers",
        args: {
            'receiver_list': frm.doc.receiver_list
        }
    })
    
    if (phone_number_list) {
        let message = ' Issue Type: ' + frm.doc.issue_type  + ' @ ' + frm.doc.location + ', of Priority: ' + frm.doc.priority + ', has been Raised by: ' + frm.doc.raised_by_name;
        frappe.call({
            method: "frappe.core.doctype.sms_settings.sms_settings.send_sms",
            args: {
                receiver_list: phone_number_list,
                msg: message,
            },
            callback: function (r) {
                if (r.exc) {
                    msgprint(r.exc);
                }
            }
        });
    }
}

const get_receivers_list = async function (frm) {
    let receivers = await frappe.call({
            method: "navari_helpdesk.controllers.receiver_list_utils.get_department_receiver_list",
            args: {
                'department': frm.doc.department
            }
        })
        
    frm.set_value('receiver_list', receivers);
}

const reopen_issue = function(frm) {
    if(frm.doc.raised_by != frappe.session.user){
        frappe.msgprint('Issues can only be reopened by the initiator')
        throw new Error("Cannot reopen Issue") 
    }
}