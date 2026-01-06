frappe.ui.form.on("Bank", {
    refresh(frm) {
        frm.page.clear_inner_toolbar();

        const button_html = `
            <span style="display:flex;align-items:center;gap:6px;">
                <i class="fa fa-university"></i>
                <span>Get Bank Details</span>
            </span>
        `;

        frm.page.add_inner_button(button_html, () => {
            if (!frm.doc.custom_ifsc_code) {
                frappe.msgprint(__("Please enter IFSC Code first"));
                return;
            }

            frappe.call({
                method: "bank_details.api.bank_details.get_bank_details_from_ifsc",
                args: {
                    custom_ifsc_code: frm.doc.custom_ifsc_code
                },
                freeze: true,
                freeze_message: __("Fetching Bank Details..."),
                callback(r) {
                    if (!r.message) return;

                    Object.keys(r.message).forEach(field => {
                        frm.set_value(field, r.message[field]);
                    });

                    frappe.show_alert({
                        message: __("Bank details fetched successfully"),
                        indicator: "green"
                    });
                }
            });
        });
    }
});
frappe.ui.form.on("Bank", {
    refresh(frm) {

        if (frm.is_new()) return;

        frappe.call({
            method: "bank_details.api.bank_details.create_bank_address",
            args: {
                bank_docname: frm.doc.name
            }
        });
    }
});
