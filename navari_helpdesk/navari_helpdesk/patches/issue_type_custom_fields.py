import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Issue Type": [
            {
                "fieldname": "department",
                "fieldtype": "Link",
                "options": "Department",
                "label": "Department",
                "translatable": 1,
                "reqd": 1,
                "in_standard_filter": 1,
                "in_list_view": 1,
                "insert_before": "description"
            },
            {
                "fieldname": "with_assets",
                "fieldtype": "Check",
                "label": "With Assets",
                "translatable": 1,
                "reqd": 0,
                "in_standard_filter": 1,
                "insert_after": "description"
            },
            {
                "fieldname": "assets_sb",
                "fieldtype": "Section Break",
                "depends_on": "with_assets",
                "label": "Assets",
                "translatable": 1,
                "insert_after": "with_assets"
            },
            {
                "fieldname": "assets",
                "fieldtype": "Table",
                "options": "Issue Type Asset",
                "label": "Assets",
                "translatable": 1,
                "mandatory_depends_on": "eval: doc.with_assets == 1",
                "insert_after": "assets_sb"
            },
        ]
    }

    create_custom_fields(custom_fields)