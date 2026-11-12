import time
import random

def email_monitor_bot():
    print("Task Bot: Email Monitoring Bot")
    print("----------------------------------")
    
    print("[Bot Status] Connecting to Gmail IMAP server...")
    time.sleep(1)
    
    print("[Bot Status] Authenticating user...")
    time.sleep(1)
    print(" Connecting to harshita.ukv@gmail.com")
    print("[Bot Status] Monitoring inbox for new emails...\n")
    
    # Simulate 5 checks
    for i in range(5):
        print(f"--- Check {i+1} ---")
        
        time.sleep(1)
        
        # 🔹 Randomly simulate unread emails (0 to 5)
        unread_count = random.randint(0, 5)
        
        if unread_count > 0:
            print(f"🚨 Alert! {unread_count} new unread email(s).")
        else:
            print("✅ No new unread emails.")
        
        time.sleep(2)   # simulate waiting (instead of 10 sec for demo)

    print("\n[Bot Status] Monitoring completed (Simulated).")


# Control Room UI
print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Email Monitor Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Email Monitor Bot...\n")
    email_monitor_bot()
    print("\n[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
