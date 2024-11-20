# Copyright (c) 2024, Vrinda and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):  
    def validate(self):  
        if not self.flight_price:  
            frappe.throw("Please provide a flight price")  
        
        total_amount = 0  
        for item in self.item:  # Corrected 'self.items' to 'self.item'
            total_amount += item.amount  

        self.total_amount = total_amount + self.flight_price
        


    def before_submit(self):
         if self.status != "Boarded":
               frappe.throw("Ticket cannot be submitted unless the status is 'Boarded'.")
    def before_insert(self):
          random_number = random.randint(1, 99)
          random_letter = random.choice("ABCDE")
          self.seat = f"{random_number} {random_letter}"


 

