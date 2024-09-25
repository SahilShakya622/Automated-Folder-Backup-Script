import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/Sahil/Pictures/Screenshots"
destination_dir = "C:/Users/Sahil/Desktop/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()  # Corrected datetime handling
    dest_dir = os.path.join(dest, str(today))  # Corrected os.path.join

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")

schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))  # Corrected lambda

while True:
    schedule.run_pending()
    time.sleep(60)
