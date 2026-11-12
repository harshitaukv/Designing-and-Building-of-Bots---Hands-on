def data_entry_bot():
    print("Task Bot: Data Entry Automation Bot")
    print("-----------------------------------")
    
    # Read data from input file
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    # Write each line into different files
    for i, line in enumerate(lines):
        filename = f"output_{i+1}.txt"
        
        with open(filename, "w") as f:
            f.write(line.strip())
        
        print(f"{filename} created successfully.")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Data Entry Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Data Entry Bot...")
    data_entry_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
