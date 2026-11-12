from openpyxl import load_workbook

def invoice_bot():
    print("Task Bot: Invoice Generation Bot")
    print("----------------------------------")
    
    wb = load_workbook("customers.xlsx")
    sheet = wb.active
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        name, product, amount = row
        
        filename = f"invoice_{name}.txt"
        
        with open(filename, "w") as f:
            f.write("----- INVOICE -----\n")
            f.write(f"Customer Name: {name}\n")
            f.write(f"Product: {product}\n")
            f.write(f"Amount: {amount}\n")
        
        print(f"{filename} generated successfully.")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Invoice Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Invoice Bot...")
    invoice_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
