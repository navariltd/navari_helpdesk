import frappe

@frappe.whitelist()
def get_allocated_to_receiver_list(allocated_to):
    receiver_list = ''
    employee_list = frappe.db.sql(
        f"""
        SELECT em.employee, em.employee_name, em.cell_number
        FROM `tabEmployee` em
        WHERE status = 'Active' AND docstatus < 2  AND IFNULL(cell_number,'') != '' AND user_id = '{allocated_to}'
        """
    )

    for emp in employee_list:
        receiver_list = receiver_list + (emp[1] + " - " + emp[2] + "\n")

    return receiver_list

@frappe.whitelist()
def get_department_receiver_list(department):
    receiver_list = ''
    employee_list = frappe.db.sql(
        f"""
        SELECT em.employee, em.employee_name, em.cell_number
        FROM `tabEmployee` em
        WHERE status = 'Active' AND docstatus < 2  AND IFNULL(cell_number,'') != '' AND department = '{department}'
        UNION
        SELECT em.employee, em.employee_name, em.cell_number
        FROM `tabEmployee` em
        WHERE em.name IN
            (SELECT hod FROM `tabDepartment`
                WHERE name IN (SELECT parent_department FROM `tabDepartment` WHERE parent_department != 'All Departments' AND name = '{department}')
            )
        """
    )

    for emp in employee_list:
        receiver_list = receiver_list + (emp[1] + " - " + emp[2] + "\n")

    return receiver_list

@frappe.whitelist()
def strip_phone_numbers(receiver_list):
    receiver_nos = []
    if receiver_list:
        for d in receiver_list.split("\n"):
            receiver_no = d
            if "-" in d:
                receiver_no = receiver_no.split("-")[1]
                if receiver_no.strip():
                    receiver_nos.append(receiver_no.strip())
    else:
        frappe.msgprint(_("Receiver List is empty. Please create Receiver List"))

    return receiver_nos
