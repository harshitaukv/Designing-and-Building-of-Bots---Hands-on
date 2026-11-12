import smtplib
from email.message import EmailMessage
sender_email = "harshitau@gmail.com"
receiver_email = "harshita.ukv@gmail.com"
app_password = "abcdefghijklmnop"  # EXACT App Password (16 chars, no spaces)
msg = EmailMessage()
msg["Subject"] = "RPA Lab – Email Automation"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("Email sent automatically using RPA Task Bot.")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully.")
