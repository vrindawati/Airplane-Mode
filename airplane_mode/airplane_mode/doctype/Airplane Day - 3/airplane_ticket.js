// Copyright (c) 2024, Vrinda and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button(__('Enter Seat Number'), function() {
            frappe.prompt([
                {
                    label: 'Seat Number',
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    reqd: 1
                }
            ],
            function(values){
                frm.set_value('seat', values.seat_number);
            },
            __('Enter Seat Number'),
            __('Submit'));
        }).addClass('btn-primary');

	},
});
