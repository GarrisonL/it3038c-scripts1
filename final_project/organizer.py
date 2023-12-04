import os
import shutil
from datetime import datetime
from collections import defaultdict

def get_directory_to_organize():
    while True:
        directory = input("Enter the directory path to organize: ")
        if os.path.exists(directory):
            return directory
        else:
            print("Error: The specified directory does not exist. Please try again.")

def log_to_file(log_file, message):
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()} - {message}\n")

def organize_files(directory, rules, log_file):
    now = datetime.now()

    for folder_name, extensions in rules.items():
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            for folder_name, ext_list in rules.items():
                if file_extension in ext_list:
                    destination_folder = os.path.join(directory, folder_name)
                    shutil.move(item_path, os.path.join(destination_folder, item))
                    log_to_file(log_file, f"Moved '{item}' to {folder_name}")
            if isinstance(ext_list, tuple) and len(ext_list) == 2:
                duration, unit = ext_list
                file_mtime = os.path.getmtime(item_path)
                file_age = now - datetime.fromtimestamp(file_mtime)
                if unit == 'days' and file_age.days > duration:
                    destination_folder = os.path.join(directory, folder_name)
                    shutil.move(item_path, os.path.join(destination_folder, item))
                    log_to_file(log_file, f"Moved '{item}' to {folder_name}")

if __name__ == "__main__":
    # Get the directory from the user
    directory_to_organize = get_directory_to_organize()

    # Define the organization rules
    organization_rules = {
        'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp'),
        'Documents': ('.pdf', '.docx', '.xlsx', '.pptx', '.txt'),
        'Archives': (30, 'days')  # Move files older than 30 days to Archives
    }

    # Create a log file
    log_file = os.path.join(directory_to_organize, 'organization_log.txt')

    # Print and log the start of organization
    print(f"Organizing files in '{directory_to_organize}'...")
    log_to_file(log_file, f"Organization started in '{directory_to_organize}'")

    # Organize files based on the rules
    organize_files(directory_to_organize, organization_rules, log_file)

    # Print and log the completion of organization
    print("Organization complete.")
    log_to_file(log_file, "Organization complete.")