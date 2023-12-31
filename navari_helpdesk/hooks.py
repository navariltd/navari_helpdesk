from . import __version__ as app_version

app_name = "navari_helpdesk"
app_title = "Navari Helpdesk"
app_publisher = "Navari Limited"
app_description = "Additional support features"
app_email = "support@navari.co.ke"
app_license = "GNU General Public License (v3)"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/navari_helpdesk/css/navari_helpdesk.css"
# app_include_js = "/assets/navari_helpdesk/js/navari_helpdesk.js"
app_include_js = [
    # "/assets/navari_helpdesk/js/navari_helpdesk.js",
    "/assets/navari_helpdesk/js/issue.js",
    "/assets/navari_helpdesk/js/todo.js"
]

# include js, css files in header of web template
# web_include_css = "/assets/navari_helpdesk/css/navari_helpdesk.css"
# web_include_js = "/assets/navari_helpdesk/js/navari_helpdesk.js"


# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "navari_helpdesk/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "navari_helpdesk.utils.jinja_methods",
#	"filters": "navari_helpdesk.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "navari_helpdesk.install.before_install"
# after_install = "navari_helpdesk.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "navari_helpdesk.uninstall.before_uninstall"
# after_uninstall = "navari_helpdesk.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "navari_helpdesk.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Issue": {
		"on_update": "navari_helpdesk.controllers.issue.on_update_issue"
	},
    "ToDo": {
		"on_update": "navari_helpdesk.controllers.todo.on_update_todo"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"navari_helpdesk.tasks.all"
#	],
#	"daily": [
#		"navari_helpdesk.tasks.daily"
#	],
#	"hourly": [
#		"navari_helpdesk.tasks.hourly"
#	],
#	"weekly": [
#		"navari_helpdesk.tasks.weekly"
#	],
#	"monthly": [
#		"navari_helpdesk.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "navari_helpdesk.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "navari_helpdesk.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "navari_helpdesk.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["navari_helpdesk.utils.before_request"]
# after_request = ["navari_helpdesk.utils.after_request"]

# Job Events
# ----------
# before_job = ["navari_helpdesk.utils.before_job"]
# after_job = ["navari_helpdesk.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"navari_helpdesk.auth.validate"
# ]
