import imaplib
import email
from collections import Counter

def email_summary_bot():
    print("Task Bot: Email Summary Bot")
    print("----------------------------------")
    
    # Connect to mail server (example: Gmail)
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Login (use your credentials)
    mail.login("your_email@gmail.com", "your_password")
    
    mail.select("inbox")
    
    # Search all emails
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    
    dates = []
    
    # Fetch emails
    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                date = msg["Date"]
                if date:
                    dates.append(date[:11])  # simple date extraction
    
    # Count emails per day
    count = Counter(dates)
    
    # Save report
    with open("email_report.txt", "w") as f:
        for day, c in count.items():
            f.write(f"{day} : {c} emails\n")
    
    print("Email summary report generated successfully.")

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
