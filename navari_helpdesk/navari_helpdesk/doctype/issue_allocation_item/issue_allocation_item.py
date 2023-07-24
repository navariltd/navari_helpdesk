# Copyright (c) 2023, Navari Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class IssueAllocationItem(Document):
	def on_submit(self):
		for item in self.items:
			if item.issue_type:
				frappe.get_doc(dict(
					doctype = 'Issue',
					subject = item.issue_type  + ' @ ' + doc.location,
					raised_by = doc.raised_by,
					raised_by_name = doc.raised_by_name,
					location = doc.location,
					department = item.department,
					hod = item.hod,
					hod_user_id = item.hod_user_id,
					receiver_list = item.receiver_list,
					issue_type = item.issue_type,
					asset = item.asset,
					asset_name = item.asset_name,
					priority = item.issue_priority,
					description = item.description,
					issue_allocation = doc.name,
					sms_sent = 1
				)).insert()
