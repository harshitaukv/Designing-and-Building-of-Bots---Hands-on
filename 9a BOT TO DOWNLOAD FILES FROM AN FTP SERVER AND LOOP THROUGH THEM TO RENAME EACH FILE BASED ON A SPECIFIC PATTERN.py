from ftplib import FTP
import os
import time
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"
DOWNLOAD_DIR = "ftp_files"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
MAX_FILES = 5
ftp = FTP(timeout=30)
ftp.connect(FTP_HOST, 21)
ftp.login(FTP_USER, FTP_PASS)
ftp.set_pasv(True)
items = ftp.nlst()
print("Items found:", items)
file_count = 0
for item in items:
    if file_count >= MAX_FILES:
        break
    if not item.lower().endswith(".jpg"):
        print(f"Skipped (not image): {item}")
        continue
    success = False
    for attempt in range(2):   # retry logic
        try:
            new_name = f"RPA_File_{file_count + 1}.jpg"
            local_path = os.path.join(DOWNLOAD_DIR, new_name)
            with open(local_path, "wb") as f:
                ftp.retrbinary(f"RETR {item}", f.write)
            print(f"Downloaded and renamed: {item} -> {new_name}")
            file_count += 1
            success = True
            break
        except Exception:
            time.sleep(1)  # wait before retry
    if not success:
        print(f"Skipped (locked/restricted): {item}")
ftp.quit()
print("FTP download and renaming process completed.")



