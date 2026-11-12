import pandas as pd
import pyperclip
import time
import pyautogui
import subprocess
# Disable failsafe for uninterrupted automation
pyautogui.FAILSAFE = False
# Step 1: Read data from Excel file
# Sample Excel file: student_data.xlsx
df = pd.read_excel("student_data.xlsx")
# Step 2: Extract required data
extracted_data = ""
for index, row in df.iterrows():
    extracted_data += f"{row['Name']} - {row['Marks']}\n"
# Step 3: Copy data to clipboard
pyperclip.copy(extracted_data)
# Step 4: Open Notepad to paste data
subprocess.Popen("notepad.exe")
time.sleep(3)
# Step 5: Paste data into Notepad
pyautogui.hotkey("ctrl", "v")
