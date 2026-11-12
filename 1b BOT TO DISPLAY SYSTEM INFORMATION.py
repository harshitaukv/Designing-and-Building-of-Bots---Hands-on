import platform
import os

def system_info_bot():
    print("Task Bot: System Information Bot")
    print("----------------------------------")
    
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Processor:", platform.processor())
    print("Machine Type:", platform.machine())
    print("Node Name:", platform.node())
    
    print("Number of CPUs:", os.cpu_count())

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("Available Task Bots:")
print("1. System Information Bot")
print("2. Exit")

choice = int(input("Select the Task Bot to execute: "))

if choice == 1:
    print("\n[Bot Status] Executing System Information Bot...")
    system_info_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
