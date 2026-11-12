import time

def unread_email_bot():
    print("Task Bot: Unread Email Counter")
    print("----------------------------------")
    
    print("[Bot Status] Connecting to Gmail IMAP server...")
    time.sleep(1)
    
    print("[Bot Status] Logging in...")
    time.sleep(1)
    
    print("[Bot Status] Accessing inbox...")
    time.sleep(1)
    
    print("[Bot Status] Searching for unread emails...")
    time.sleep(2)
    
    # 🔹 FAKE unread email count
    unread_count = 536
    print("From: harshita.ukv@gmail.com")
    print("\n====================================")
    print(f"Number of unread emails: {unread_count}")
    print("====================================")
    
    print("\n[Bot Status] Process completed (Simulated).")

# Run bot
unread_email_bot()
