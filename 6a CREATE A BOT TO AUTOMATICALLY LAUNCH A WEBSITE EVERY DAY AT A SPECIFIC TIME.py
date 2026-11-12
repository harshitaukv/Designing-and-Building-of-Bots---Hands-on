import webbrowser
import datetime
# Website to be launched
url = "https://news.google.com"
print("Task Bot: Scheduled Website Launcher")
print("Current Date and Time:", datetime.datetime.now())
# Open the website
webbrowser.open(url)
print("Website launched successfully.")
