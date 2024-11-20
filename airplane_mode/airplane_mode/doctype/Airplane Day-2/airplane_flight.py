# Copyright (c) 2024, Vrinda and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
# from frappe.website.website_generator import WebsiteGenerator

# class AirplaneFlight(WebsiteGenerator):
#     def validate(self):
#         super().validate()  # Ensure base class validation is called
#         if self.is_flight_completed():
#             self.status = "Completed"

#     def is_flight_completed(self):
#         # Check if both departure_time and arrival_time are set
#         return bool(self.departure_time and self.arrival_time)

# @frappe.whitelist(allow_guest=True)
# def show_me(flight_name):
#     try:
#         flight = frappe.get_doc("Airplane Flight", flight_name)
#         if not flight.is_published:
#             frappe.throw(_("Flight document is not published."), frappe.DoesNotExistError)
#         return frappe.render_template("your_app_name/templates/web/showme.html", {"flight": flight})
#     except frappe.DoesNotExistError:
#         frappe.local.response.status_code = 404
#         return "Flight document not found."
#     except Exception as e:
#         frappe.local.response.status_code = 500
#         return str(e)

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        # Set the status to "Completed" when the document is submitted
        self.status = "Completed"
        self.save()