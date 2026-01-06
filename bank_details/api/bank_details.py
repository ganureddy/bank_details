import frappe
import requests


@frappe.whitelist()
def get_bank_details_from_ifsc(custom_ifsc_code):
    """
    Fetch bank details using IFSC and return values
    (DO NOT save document here)
    """

    if not custom_ifsc_code:
        frappe.throw("IFSC Code is required")

    url = f"https://ifsc.razorpay.com/{custom_ifsc_code}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        bank_name = data.get("BANK") or ""

        return {
            "bank_name": f"{bank_name} - {custom_ifsc_code}" if bank_name else custom_ifsc_code,
            "custom_bank_code": data.get("BANKCODE") or "",
            "custom_branch": data.get("BRANCH") or "",
            "custom_address": data.get('ADDRESS') or "",
            "custom_city": data.get("CITY") or "",
            "custom_district": data.get("DISTRICT") or "",
            "custom_state": data.get("STATE") or "",
            "custom_micr": data.get("MICR") or "",
            "swift_number": data.get("SWIFT") or "",
            "custom_contact": data.get("CONTACT") or "",
            "custom_neft_enabled": 1 if data.get("NEFT") else 0,
            "custom_rtgs_enabled": 1 if data.get("RTGS") else 0,
            "custom_imps_enabled": 1 if data.get("IMPS") else 0,
            "custom_upi_enabled": 1 if data.get("UPI") else 0,
        }

    except Exception:
        frappe.log_error(frappe.get_traceback(), "IFSC Fetch Error")
        frappe.throw("Unable to fetch bank details. Please check IFSC code.")



@frappe.whitelist()
def create_bank_address(bank_docname):
    """
    Create Address for Bank after save
    """

    if not bank_docname:
        frappe.throw("Bank document name is required")

    bank = frappe.get_doc("Bank", bank_docname)

    # Prevent duplicate Address
    existing = frappe.db.exists(
        "Address",
        {
            "address_title": bank.bank_name,
            "address_type": "Billing"
        }
    )

    if existing:
        return {"status": "skipped", "message": "Address already exists"}

    address = frappe.new_doc("Address")
    address.address_title = bank.bank_name
    address.address_type = "Billing"

    address.address_line1 = bank.custom_address
    address.city = bank.custom_city
    address.state = bank.custom_state
    address.county = bank.custom_district
    address.country = "India"

    address.append(
        "links",
        {
            "link_doctype": "Bank",
            "link_name": bank.name
        }
    )

    address.flags.ignore_permissions = True
    address.insert()

    return {"status": "success", "message": "Address created"}
