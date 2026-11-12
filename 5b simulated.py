import time
from collections import Counter

def email_summary_bot():
    print("Task Bot: Email Summary Bot")
    print("----------------------------------")
    
    print("\n[Bot Status] Connecting to Gmail server...")
    time.sleep(1)
    
    print("[Bot Status] Authenticating user...")
    time.sleep(1)
    
    print("[Bot Status] Accessing inbox...")
    time.sleep(1)
    
    # 🔹 FAKE EMAIL DATA (simulated inbox)
    fake_dates = [
        " From: harshita.ukv@gmail.com\n"
        "Mon, 01 Apr", "Mon, 01 Apr",
        "Tue, 02 Apr",
        "Wed, 03 Apr", "Wed, 03 Apr", "Wed, 03 Apr",
        "Thu, 04 Apr",
        "Fri, 05 Apr", "Fri, 05 Apr"
    ]
    
    print("[Bot Status] Fetching emails...")
    time.sleep(2)
    
    # Count emails per day
    count = Counter(fake_dates)
    
    print("[Bot Status] Analyzing email data...")
    time.sleep(1)
    
    # Display summary
    print("\n========== EMAIL SUMMARY ==========")
    for day, c in count.items():
        print(f"{day} : {c} emails")
    print("===================================")
    
    # Save report
    with open("email_report.txt", "w") as f:
        for day, c in count.items():
            f.write(f"{day} : {c} emails\n")
    
    print("\n[Bot Status] Report saved to email_report.txt")
    print("[Bot Status] Email summary generated successfully (Simulated).")


# Control Room
print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Email Summary Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Email Summary Bot...")
    email_summary_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
