import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Issue Allocation Item": [
            {
                "fieldname": "receiver_list",
                "fieldtype": "Code",
                "insert_after": "hod_user_id",
                "label": "Receiver List",
            }
        ]
    }

    create_custom_fields(custom_fields)