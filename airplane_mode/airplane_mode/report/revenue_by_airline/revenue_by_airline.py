# Copyright (c) 2024, Vrinda and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# import frappe

# def execute(filters=None):
#     # Query to fetch the revenue by airline
#     query = """
#         SELECT 
#             airline.name AS "Airline:Link/Airline", 
#             COALESCE(SUM(ticket.ticket_price), 0) AS "Revenue:Currency/Revenue"  # Use the correct field name
#         FROM 
#             `tabAirline` AS airline
#         LEFT JOIN 
#             `tabAirplane Ticket` AS ticket ON ticket.airline = airline.name
#         WHERE 
#             ticket.status IN ('Booked', 'Confirmed', 'Checked-In', 'Boarded', 'Completed')  # Relevant statuses
#         GROUP BY 
#             airline.name
#         ORDER BY 
#             `Revenue:Currency/Revenue` DESC;
#     """

#     # Fetch the results from the database
#     results = frappe.db.sql(query, as_dict=True)

#     # Calculate the total revenue
#     total_revenue = sum([row['Revenue'] for row in results])

#     # Adding a total row at the end
#     results.append({
#         "Airline": "Total",
#         "Revenue": total_revenue
#     })

#     # Return the results to display in the report
#     return results


import frappe  
from frappe import _  

def execute(filters=None):  
    revenue_data = frappe.db.sql("""  
        SELECT  
            a.name AS airline,  
            IFNULL(SUM(at.flight_price), 0) AS revenue  
        FROM  
            tabAirline AS a  
        LEFT JOIN  
            `tabAirplane Ticket` AS at ON at.flight = a.name  
        GROUP BY  
            a.name  
    """, as_dict=True)  

    total_revenue = 0  
    columns = [  
        {  
            "fieldname": "airline",  
            "label": _("Airline"),  
            "fieldtype": "Link",  
            "options": "Airline",  
            "width": 200  
        },  
        {  
            "fieldname": "revenue",  
            "label": _("Revenue"),  
            "fieldtype": "Currency",  
            "width": 150  
        }  
    ]  

    formatted_data = []  
    chart_data = {  
        "labels": [],  
        "datasets": [{  
            "name": _("Revenue by Airline"),  
            "values": []  
        }]  
    }  

    # Process revenue data  
    for item in revenue_data:  
        formatted_data.append(item)  
        total_revenue += item.revenue  

        chart_data["labels"].append(item.airline)  
        chart_data["datasets"][0]["values"].append(item.revenue)  

    # Add total revenue to the formatted data and chart  
    formatted_data.append({  
        "airline": "Total",  
        "revenue": total_revenue  
    })  

    chart_data["labels"].append("Total")  
    chart_data["datasets"][0]["values"].append(total_revenue)  

    # Chart options  
    chart_options = {  
        "title": _("Revenue Distribution by Airline"),  
        "type": "donut",  
        "data": chart_data,  
        "colors": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"],   
        "donut": {  
            "title": _("Total Revenue: {0}".format(total_revenue)),  
            "label": _("Revenue")  
        }  
    }  

    return columns, formatted_data, chart_options