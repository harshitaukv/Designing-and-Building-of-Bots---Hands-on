from openpyxl import load_workbook
from queue import Queue

def ticket_bot():
    print("Task Bot: Ticket Prioritization Bot")
    print("------------------------------------")
    
    wb = load_workbook("tickets.xlsx")
    sheet = wb.active
    
    high_priority_queue = Queue()
    
    # Read tickets from Excel
    for row in sheet.iter_rows(min_row=2, values_only=True):
        ticket_id, priority = row
        
        if priority.lower() == "high":
            high_priority_queue.put(ticket_id)
    
    # Assign to senior agents
    agent = 1
    
    with open("assigned_tickets.txt", "w") as f:
        while not high_priority_queue.empty():
            ticket = high_priority_queue.get()
            assignment = f"Ticket {ticket} -> Senior Agent {agent}"
            print(assignment)
            f.write(assignment + "\n")
            agent += 1
    
    print("High-priority tickets assigned successfully.")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Ticket Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Ticket Bot...")
    ticket_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
