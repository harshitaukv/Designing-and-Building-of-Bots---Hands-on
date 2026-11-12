import subprocess
import time
import pyautogui
# Disable fail-safe to avoid accidental interruption
pyautogui.FAILSAFE = False
# Step 1: Open Notepad
subprocess.Popen("notepad.exe")
time.sleep(3)   # ensure Notepad opens fully
# Step 2: Type text into Notepad
text = (
    "Robotic Process Automation Laboratory\n"
    "Exercise 2A: Automating Data Entry using Notepad\n"
    "This content was generated automatically by a Task Bot."
)
pyautogui.write(text, interval=0.05)
# Step 3: Save the file
pyautogui.hotkey("ctrl", "s")
time.sleep(2)
# Step 4: Enter file name and save
pyautogui.write("RPA_DataEntry.txt", interval=0.05)
pyautogui.press("enter")
