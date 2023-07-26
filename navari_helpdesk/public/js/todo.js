let message, changed_field

frappe.ui.form.on('ToDo', {
    department: function (frm) {
        if (frm.doc.department && frm.doc.reference_type == 'Issue') {
            get_department_receivers_list(frm);
            changed_field = "department";
            frm.set_value('sms_sent', 0);
        }
    },
    allocated_to: function (frm) {
        if (frm.doc.allocated_to && frm.doc.reference_type == 'Issue') {
            get_issue_assignees_list(frm);
            changed_field = "allocated_to";
            frm.set_value('sms_sent', 0);
        }
    }
});

let send_sms = function (frm) {
    frappe.call({
        method: "navari_helpdesk.controllers.receiver_list_utils.strip_phone_numbers",
        args: {
            'receiver_list': frm.doc.receiver_list
        },
        callback: function (response) {
            if (response.message) {
                if (changed_field == 'allocated_to') {
                    message = ' Issue Type: ' + frm.doc.issue_type  + ' @ ' + frm.doc.location + ', of Priority: ' + frm.doc.priority + ', has been assigned to you';
                } else if (changed_field == 'department') {
                    message = ' Issue Type: ' + frm.doc.issue_type  + ' @ ' + frm.doc.location + ' of Priority: ' + frm.doc.priority + ', has been moved to your department';
                }  

                frappe.call({
                    method: "frappe.core.doctype.sms_settings.sms_settings.send_sms",
                    args: {
                        receiver_list: response.message,
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
    })
}

let get_department_receivers_list = function (frm) {
    frappe.call({
            method: "navari_helpdesk.controllers.receiver_list_utils.get_department_receiver_list",
            args: {
                'department': frm.doc.department
            },
            callback: function (response) {
               if (response.message) {
                   frm.set_value('receiver_list', response.message)
               } 
            }
        })
        
}

let get_issue_assignees_list = function (frm) {
    frappe.call({
            method: "navari_helpdesk.controllers.receiver_list_utils.get_allocated_to_receiver_list",
            args: {
                'allocated_to': frm.doc.allocated_to
            },
            callback: function (response) {
                if (response.message) {
                    frm.set_value('receiver_list', response.message)     
                }
            }
        })
        
}