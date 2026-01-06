# Bank Details

A custom ERPNext / Frappe app to **fetch and auto-populate Bank details using IFSC code**.

- Fetch bank details on a single click
- Auto-fill Bank master fields before saving
- Maintain clean and accurate bank records
- Use a modern, user-friendly UI button on the Bank form

---

## ✨ Features

- 🔍 Fetch bank details using **IFSC code**
- 🏦 Auto-populates:
  - Bank Name (Bank + IFSC)
  - Bank Code
  - Branch
  - Address
  - City, District, State
  - MICR
  - SWIFT
  - NEFT / RTGS / IMPS / UPI availability
- 🖱️ **Get Bank Details** button available on **new Bank form**
- 🚫 No auto-save — user reviews data before saving
- ⚙️ Naming Series support (auto-configured on install)
- 🔒 No API keys required

---

## 🧩 Tech Stack

- Frappe Framework v16
- ERPNext v16

---

## 🚀 Installation

Install the app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/ganureddy/bank_details --branch main
bench install-app bank_details
