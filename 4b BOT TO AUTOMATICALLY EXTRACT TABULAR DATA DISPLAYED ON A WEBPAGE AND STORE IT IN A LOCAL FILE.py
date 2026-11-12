import requests
from bs4 import BeautifulSoup

def web_table_bot():
    print("Task Bot: Web Data Extraction Bot")
    print("----------------------------------")
    
    url = "https://www.w3schools.com/html/html_tables.asp"   # replace with actual webpage
    
    # Get webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find table
    table = soup.find("table")
    
    rows = table.find_all("tr")
    
    extracted_data = []
    
    for row in rows:
        cols = row.find_all(["td", "th"])
        col_data = [col.text.strip() for col in cols]
        extracted_data.append(" | ".join(col_data))
    
    # Save to file
    with open("web_data.txt", "w") as f:
        for line in extracted_data:
            f.write(line + "\n")
    
    print("Table data extracted and saved to web_data.txt")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run Web Extraction Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing Web Extraction Bot...")
    web_table_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
