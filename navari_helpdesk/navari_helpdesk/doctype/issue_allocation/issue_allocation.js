// Copyright (c) 2023, Navari Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Issue Allocation', {
	onload: function (frm) {
        cur_frm.set_query("issue_type", "items", function(frm, cdt, cdn) {
            let d = locals[cdt][cdn];
            return {
                "filters": {
                    "department": d.department
                }
            };
        });
    },
    on_submit: function (frm) {
        send_sms(frm);
    }
})

frappe.ui.form.on("Issue Allocation Item", "department", async function (frm, cdt, cdn) {
    let d = locals[cdt][cdn];
    
    let receivers_list = await frappe.call({
        method: "navari_helpdesk.controllers.receiver_list_utils.get_department_receiver_list",
        args: {
            'department': d.department
        }
    })
    
    d.receiver_list = receivers_list
    
    frappe.db.get_value("Department", { "name": d.department }, "hod", function (value) {
        d.hod = value.hod;
        if (d.hod)
            frappe.model.with_doc('Employee', d.hod, function () {
                let emp = frappe.model.get_doc('Employee', d.hod);
                d.hod_user_id = emp.user_id;
            });
            
    });
})

const send_sms = function (frm) {
    let phone_number_list;
    $.each(frm.doc.items, async function (i, row) {
        if(row.receiver_list) {
            phone_number_list = await frappe.call({
                method: "navari_helpdesk.controllers.receiver_list_utils.strip_phone_numbers",
                args: {
                    'receiver_list': row.receiver_list
                }
            })
        }
        
        if (phone_number_list) {
            let message = ' Issue Type: ' + row.issue_type  + ' @ ' + frm.doc.location + ', of Priority: ' + row.issue_priority + ', has been Raised by: ' + frm.doc.raised_by_name;
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
    });
};