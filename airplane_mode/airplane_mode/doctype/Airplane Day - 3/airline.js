// Copyright (c) 2024, Vrinda and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {
//         if (frm.doc.website) {
//             frm.add_custom_button(__('Visit Website'), function() {
//                 window.open(frm.doc.website, '_blank');
//             }).addClass('btn-primary');
//         }
//     },
// });


frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // If the website field is not empty, add a custom button to open the website
        if (frm.doc.website) {
            frm.add_custom_button(('Visit Website'), function() {
                window.open(frm.doc.website, '_blank'); // Opens the website in a new tab
            });
        }
    },

    onload: function(frm) { // Correct event name is 'onload', not 'on_load'
        // If the website field is not empty, add a web link
        if (frm.doc.website) {
            frm.add_web_link(('Visit Official Website'), frm.doc.website); // Correct syntax for add_web_link
        }
    }
});