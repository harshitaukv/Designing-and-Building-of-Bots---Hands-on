import time

def ftp_file_bot():
    print("Task Bot: FTP File Transfer Bot")
    print("----------------------------------")
    
    print("[Bot Status] Connecting to FTP server...")
    time.sleep(1)
    
    print("[Bot Status] Logging in...")
    time.sleep(1)
    
    print("[Bot Status] Accessing /source directory...")
    time.sleep(1)
    
    # 🔹 Fake file list
    files = [
        "report1.txt",
        "image1.jpg",
        "notes.txt",
        "photo.jpg",
        "data.csv",
        "presentation.pptx",
        "diagram.jpg"
    ]
    
    print("\nFiles found:", files)
    print("\n[Bot Status] Processing files...\n")
    time.sleep(1)
    
    for file in files:
        time.sleep(0.5)
        
        if file.endswith(".txt"):
            print(f"{file} moved to /text_files/{file}")
        
        elif file.endswith(".jpg"):
            print(f"{file} moved to /images/{file}")
        
        else:
            print(f"Skipped (unsupported type): {file}")
    
    print("\n[Bot Status] Closing FTP connection...")
    time.sleep(1)
    
    print("File transfer completed (Simulated).")


# Control Room UI
print("==========================================")
print("        AUTOMATION ANYWHERE CONTROL ROOM   ")
print("==========================================")
print("1. Run FTP File Bot")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\n[Bot Status] Executing FTP File Bot...\n")
    ftp_file_bot()
    print("\n[Bot Status] Execution Completed.")

else:
    print("Exiting Control Room...")
