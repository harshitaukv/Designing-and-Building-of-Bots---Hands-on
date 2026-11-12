import time

def fake_email_bot():
    print("Task Bot: Email Automation Bot")
    print("----------------------------------")
    
    sender_email = "harshitau2105@gmail.com"
    receiver_email = "harshita.ukv@gmail.com"   # 👈 put your email here
    
    subject = "RPA Lab – Email Automation"
    message = """This email was sent automatically using a Task Bot.
Robotic Process Automation Laboratory."""
    
    print("\n[Bot Status] Connecting to Gmail server...")
    time.sleep(1)
    
    print("[Bot Status] Authenticating user...")
    time.sleep(1)
    
    print("[Bot Status] Preparing email...")
    time.sleep(1)
    
    # 📧 Gmail-style preview
    print("\n================ GMAIL VIEW =================")
    print(f"{subject}    [Inbox]")
    print(f"\nFrom: {sender_email}")
    print(f"To: harshita.ukv@gmail.com")
    print("\n--------------------------------------------")
    print(message)
    print("============================================")
    
    time.sleep(1)
    print("\n[Bot Status] Sending email...")
    time.sleep(2)
    
    print("[Bot Status] Email sent successfully.")
    
    # Save as "inbox style"
    with open("fake_email.txt", "w") as f:
        f.write(f"{subject}    [Inbox]\n\n")
        f.write(f"From: {sender_email}\n")
        f.write("To: me\n\n")
        f.write(message)

    print("[Bot Status] Email saved to RPA_email.txt")

# Control Room
print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Email Automation Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Email Bot...")
    fake_email_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
