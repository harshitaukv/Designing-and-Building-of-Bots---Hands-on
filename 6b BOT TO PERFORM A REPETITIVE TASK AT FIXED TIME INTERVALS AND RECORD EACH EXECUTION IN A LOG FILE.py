import time
from datetime import datetime

def repetitive_task_bot():
    print("Task Bot: Repetitive Task Bot")
    print("----------------------------------")
    
    for i in range(5):   # run 5 times
        current_time = datetime.now()
        
        # Perform simple task
        print(f"Task executed at {current_time}")
        
        # Log execution
        with open("log.txt", "a") as f:
            f.write(f"Execution {i+1} at {current_time}\n")
        
        time.sleep(5)   # wait 5 seconds

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Repetitive Task Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Repetitive Task Bot...")
    repetitive_task_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
