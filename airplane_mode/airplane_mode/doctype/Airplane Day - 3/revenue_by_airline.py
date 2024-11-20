# Copyright (c) 2024, Vrinda and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

import frappe

def execute(filters=None):
    # Query to fetch the revenue by airline
    query = """
        SELECT 
            airline.name AS "Airline:Link/Airline", 
            COALESCE(SUM(ticket.ticket_price), 0) AS "Revenue:Currency/Revenue"  # Use the correct field name
        FROM 
            `tabAirline` AS airline
        LEFT JOIN 
            `tabAirplane Ticket` AS ticket ON ticket.airline = airline.name
        WHERE 
            ticket.status IN ('Booked', 'Confirmed', 'Checked-In', 'Boarded', 'Completed')  # Relevant statuses
        GROUP BY 
            airline.name
        ORDER BY 
            `Revenue:Currency/Revenue` DESC;
    """

    # Fetch the results from the database
    results = frappe.db.sql(query, as_dict=True)

    # Calculate the total revenue
    total_revenue = sum([row['Revenue'] for row in results])

    # Adding a total row at the end
    results.append({
        "Airline": "Total",
        "Revenue": total_revenue
    })

    # Return the results to display in the report
    return results
