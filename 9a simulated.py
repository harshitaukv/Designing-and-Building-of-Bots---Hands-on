import time
import os

DOWNLOAD_DIR = "ftp_files"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def fake_ftp_bot():
    print("Task Bot: FTP File Download Bot")
    print("----------------------------------")
    
    print("[Bot Status] Connecting to FTP server...")
    time.sleep(1)
    
    print("[Bot Status] Authenticating user...")
    time.sleep(1)
    
    print("[Bot Status] Fetching file list...\n")
    time.sleep(1)

    # 🔹 Fake FTP file list (similar to your screenshot)
    items = [
        "10.101.1.2_20251213-10460295_VVA.jpg",
        "10.101.1.2_20251213-10460465_VVA.jpg",
        "test_upload.bin",
        "upload-test-file.jpg",
        "10.101.1.2_20251213-10460755_VVA.jpg",
        "10.101.1.2_20251213-10460912_VVA.jpg",
        "data.txt",
        "image_backup.png",
        "10.101.1.2_20251213-10461001_VVA.jpg"
    ]

    print("Items found:", items)

    MAX_FILES = 5
    file_count = 0

    for item in items:
        if file_count >= MAX_FILES:
            break
        
        time.sleep(0.5)

        # Skip non-jpg files
        if not item.lower().endswith(".jpg"):
            print(f"Skipped (not image): {item}")
            continue
        
        # 🔹 Simulate locked/restricted file
        if "10460912" in item:
            print(f"Skipped (locked/restricted): {item}")
            continue
        
        # Simulate download
        new_name = f"RPA_File_{file_count + 1}.jpg"
        local_path = os.path.join(DOWNLOAD_DIR, new_name)
        
        # Create dummy file (simulation)
        with open(local_path, "w") as f:
            f.write("Fake image content")
        
        print(f"Downloaded and renamed: {item} -> {new_name}")
        file_count += 1

    print("\n[Bot Status] FTP download and renaming process completed.")


# Run
fake_ftp_bot()
