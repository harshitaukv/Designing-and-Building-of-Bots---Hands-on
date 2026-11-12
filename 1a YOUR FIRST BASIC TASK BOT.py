
def task_bot_1():
    print("Task Bot 1: Greeting Bot")
    print("Hello! Welcome to Robotic Process Automation.")

def task_bot_2():
    print("Task Bot 2: Date and Time Bot")
    from datetime import datetime
    print("Current Date and Time:", datetime.now())

def task_bot_3():
    print("Task Bot 3: Simple Calculation Bot")
    a, b = 10, 5
    print("Addition:", a + b)
    print("Multiplication:", a * b)
print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("Available Task Bots:")
print("1. Greeting Bot")
print("2. Date and Time Bot")
print("3. Calculation Bot")
print("4. Exit")
choice = int(input("Select the Task Bot to execute: "))

if choice == 1:
    print("\n[Bot Status] Executing Greeting Bot...")
    task_bot_1()
    print("[Bot Status] Execution Completed.")

elif choice == 2:
    print("\n[Bot Status] Executing Date and Time Bot...")
    task_bot_2()
    print("[Bot Status] Execution Completed.")

elif choice == 3:
    print("\n[Bot Status] Executing Calculation Bot...")
    task_bot_3()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
