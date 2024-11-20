import frappe

def get_context(context):
    airports = frappe.get_all("Shop", fields=["DISTINCT airport as name"])

    airport_shop_counts = {}


    for airport in airports:
        airport_name = airport['name']
        shop_count = frappe.db.count("Shop", filters={"status": "Available", "airport": airport_name})
        airport_shop_counts[airport_name] = shop_count

    context.airports = airports
    context.airport_shop_counts = airport_shop_counts  # Pass the shop counts to the context
    context.selected_airport = frappe.form_dict.get('airport')