import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Issue": [
            {
                "fieldname": "location",
                "fieldtype": "Link",
                "in_list_view": 1,
                "in_standard_filter": 1,
                "insert_after": "customer",
                "label": "Location",
                "options": "Location",
                "reqd": 1,
            },
            {
                "fieldname": "department",
                "fieldtype": "Link",
                "in_list_view": 1,
                "in_standard_filter": 1,
                "label": "Department",
                "options": "Department",
                "reqd": 1,
            },
            {
                "fieldname": "issue_column_break_6",
                "fieldtype": "Column Break",
                "insert_after": "department",
            },
            {
                "fieldname": "hod",
                "fieldtype": "Link",
                "insert_after": "issue_column_break_6",
                "label": "HOD",
                "options": "Employee",
                "read_only": 1,
            },
            {
                "fieldname": "hod_name",
                "fetch_from": "hod.employee_name",
                "fieldtype": "Data",
                "insert_after": "hod",
                "label": "HOD Name",
                "read_only": 1,
                "translatable": 1
            },
            {
                "fieldname": "hod_user_id",
                "fieldtype": "Link",
                "insert_after": "hod_namr",
                "label": "HOD User Id",
                "options": "User",
                "read_only": 1,
            },
            {
                "fieldname": "raised_by_name",
                "fieldtype": "Data",
                "bold": 1,
                "fetch_from": "raised_by.full_name",
                "fetch_if_empty": 1,
                "insert_after": "raised_by",
                "label": "Raised by Name",
                "reqd": 1,
                "translatable": 1,
            },
            {
                "fieldname": "asset",
                "fieldtype": "Link",
                "in_standard_filter": 1,
                "insert_after": "issue_type",
                "label": "Asset",
                "options": "Asset",
            },
            {
                "fieldname": "asset_name",
                "fieldtype": "Data",
                "fetch_from": "asset.asset_name",
                "fetch_if_empty": 0,
                "label": "Asset Name",
                "read_only": 1,
                "translatable": 1
            },
            {
                "fieldname": "details_tab",
                "fieldtype": "Tab Break",
                "insert_after": "issue_split_from",
                "label": "Description",
            },
            {
                "fieldname": "sla_tab",
                "fieldtype": "Tab Break",
                "insert_after": "description",
                "label": "Service Level Agreement Details",
            },
            {
                "fieldname": "receiver_list_tab",
                "fieldtype": "Tab Break",
                "insert_after": "user_resolution_time",
                "label": "Receiver List",
            },
            {
                "fieldname": "receiver_list_section",
                "collapsible": 1,
                "fieldtype": "Section Break",
                "insert_after": "receiver_list_tab",
                "label": "Receiver List",
            },
            {
                "fieldname": "receiver_list",
                "fieldtype": "Code",
                "insert_after": "receiver_list_section",
                "label": "Receiver List",
            },
            {
                "fieldname": "issue_allocation",
                "fieldtype": "Link",
                "insert_after": "additional_info",
                "label": "Issue Allocation",
                "options": "Issue Allocation",
            },
            {
                "fieldname": "sms_sent",
                "fieldtype": "Check",
                "insert_after": "issue_allocation",
                "label": "SMS Sent",
            }
        ]
    }

    create_custom_fields(custom_fields)