import frappe

def on_update_issue(doc, method=None):
    if(doc.status == 'Closed' or doc.status == 'Resolved'):
        to_do_list = frappe.db.get_all('ToDo',
            filters = {
                'reference_name': doc.name
            }
        )

        for todo in to_do_list:
            current_todo = frappe.get_doc('ToDo', todo.name)
            current_todo.status = 'Closed'
            current_todo.save()