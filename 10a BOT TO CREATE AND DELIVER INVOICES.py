import os
from datetime import date

# Invoice directory
INVOICE_DIR = "invoices"
os.makedirs(INVOICE_DIR, exist_ok=True)

# Invoice details
invoice_number = "INV1002"
customer_name = "ABC Technologies"
product = "Software Subscription"
amount = 15000
invoice_date = date.today()


# Create invoice content

invoice_content = f"""
-------------------------------
           INVOICE
-------------------------------
Invoice No : {invoice_number}
Date       : {invoice_date}
Customer   : {customer_name}
Item       : {product}
Amount     : Rs.{amount}
Status     : Generated Automatically
-------------------------------
"""

# Save invoice to file

invoice_path = os.path.join(INVOICE_DIR, f"{invoice_number}.txt")
with open(invoice_path, "w") as file:
    file.write(invoice_content)
print("Invoice created successfully.")
print("Invoice saved at:", invoice_path)






