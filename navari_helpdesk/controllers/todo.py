import frappe

def on_update_todo(doc, method=None):
    if (doc.reference_type == 'Issue'):
        issue_doc = frappe.get_doc('Issue', doc.reference_name)
        frappe.db.set_value('ToDo', doc.name, 'location', issue_doc.location)
        frappe.db.set_value('ToDo', doc.name, 'department', issue_doc.department)
        frappe.db.set_value('ToDo', doc.name, 'issue_type', issue_doc.issue_type)
