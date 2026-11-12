from ftplib import FTP

def ftp_file_bot():
    print("Task Bot: FTP File Transfer Bot")
    print("----------------------------------")
    
    ftp = FTP("ftp.example.com")
    ftp.login("username", "password")
    
    ftp.cwd("/source")   # source folder
    files = ftp.nlst()
    
    for file in files:
        if file.endswith(".txt"):
            ftp.rename(file, f"/text_files/{file}")
            print(f"{file} moved to text_files folder")
        
        elif file.endswith(".jpg"):
            ftp.rename(file, f"/images/{file}")
            print(f"{file} moved to images folder")
    
    ftp.quit()
    print("File transfer completed.")

print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run FTP File Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing FTP File Bot...")
    ftp_file_bot()
    print("[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
