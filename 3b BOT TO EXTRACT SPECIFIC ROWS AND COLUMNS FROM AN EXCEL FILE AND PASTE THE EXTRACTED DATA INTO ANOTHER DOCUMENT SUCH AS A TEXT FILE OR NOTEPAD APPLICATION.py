from openpyxl import load_workbook

def excel_to_text_bot():
    print("Task Bot: Excel Data Extraction Bot")
    print("------------------------------------")
    
    # Load Excel file
    wb = load_workbook("data.xlsx")
    sheet = wb.active
    
    extracted_data = []
    
    # Example: Extract rows 1 to 3 and columns 1 to 2
    for row in sheet.iter_rows(min_row=1, max_row=3, min_col=1, max_col=2):
        row_data = []
        for cell in row:
            row_data.append(str(cell.value))
        extracted_data.append(" ".join(row_data))
    
    # Write to text file
    with open("output.txt", "w") as f:
        for line in extracted_data:
            f.write(line + "\n")
    
    print("Data extracted and saved to output.txt successfully.")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Excel Extraction Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Excel Extraction Bot...")
    excel_to_text_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
