import imaplib
import time

def email_monitor_bot():
    print("Task Bot: Email Monitoring Bot")
    print("----------------------------------")
    
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("your_email@gmail.com", "your_password")
    
    for i in range(5):   # check 5 times
        mail.select("inbox")
        
        status, messages = mail.search(None, "UNSEEN")
        unread_ids = messages[0].split()
        
        if len(unread_ids) > 0:
            print(f"Alert! {len(unread_ids)} new unread email(s).")
        else:
            print("No new unread emails.")
        
        time.sleep(10)   # check every 10 seconds

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Email Monitor Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Email Monitor Bot...")
    email_monitor_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
