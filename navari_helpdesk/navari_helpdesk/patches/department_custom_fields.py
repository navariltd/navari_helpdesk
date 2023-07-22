import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Department": [
            {
                "fieldname": "hod",
                "fieldtype": "Link",
                "options": "Employee",
                "label": "HOD",
                "translatable": 1,
                "reqd": 1,
                "in_standard_filter": 1,
                "in_list_view": 1,
                "insert_after": "column_break_3"
            },
            {
                "fieldname": "employee_name",
                "fieldtype": "Data",
                "options": "Employee",
                "label": "Employee Name",
                "translatable": 1,
                "reqd": 1,
                "in_standard_filter": 0,
                "in_list_view": 0,
                "fetch_from": "hod.employee_name",
                "read_only": 1,
                "insert_after": "hod",
            },
        ]
    }

    create_custom_fields(custom_fields)