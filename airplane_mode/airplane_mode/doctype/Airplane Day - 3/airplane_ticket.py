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


def validate_ticket_creation(doc, method):
    airplane = frappe.get_doc("Airplane", doc.airplane)
    existing_tickets = frappe.db.count('Airplane Ticket', {'flight': doc.flight})
    if existing_tickets >= airplane.capacity:
        frappe.throw(f"Cannot create ticket. Airplane capacity of {airplane.capacity} is full.")


import frappe

def before_insert(doc, method):
    airplane = frappe.get_doc('Airplane', doc.airplane)
    current_tickets = frappe.db.count('Airplane Ticket', {'airplane': doc.airplane})

    if current_tickets >= airplane.capacity:
        frappe.throw(f'The airplane has reached its capacity of {airplane.capacity} seats.')


import frappe

def before_insert(doc, method):
    flight = frappe.get_doc('Airplane Flight', doc.flight)
    airplane = frappe.get_doc('Airplane', flight.airplane)
    current_tickets = frappe.db.count('Airplane Ticket', {'flight': doc.flight})
    if current_tickets >= airplane.capacity:
        frappe.throw(f'The airplane has reached its capacity of {airplane.capacity} seats. Cannot book more tickets.')