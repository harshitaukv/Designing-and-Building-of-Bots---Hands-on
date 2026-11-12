import imaplib
# Email credentials
EMAIL = "harshita.ukv@gmail.com"
APP_PASSWORD = "abcdefghijklmnop"   # Your 16-character App Password (no spaces)
# Step 1: Connect to Gmail IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
# Step 2: Login
mail.login(EMAIL, APP_PASSWORD)
# Step 3: Select inbox
mail.select("inbox")
# Step 4: Search for unread emails
status, messages = mail.search(None, "UNSEEN")
# Step 5: Count unread emails
unread_count = len(messages[0].split())
print("Number of unread emails:", unread_count)
# Step 6: Logout
mail.logout()
