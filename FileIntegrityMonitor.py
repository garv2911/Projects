import hashlib
import os
import json
import time

HASH_STORAGE_FILE ="file_hashes.json"

def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    try: 
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                file_hashes[file_path] = file_hash
    return file_hashes

def monitor_changes(directory, interval=10):
    if os.path.exists(HASH_STORAGE_FILE):
        with open(HASH_STORAGE_FILE, "r") as f:
            previous_hashes = json.load(f)
    else:
        previous_hashes = {}

    while True:
        print("\nScanning for changes...\n")
        current_hashes = scan_directory(directory)
        modified_files = []
        new_files = []
        deleted_files = []

        for file, hash_value in current_hashes.items():
            if file in previous_hashes:
                if previous_hashes[file] != hash_value:
                    modified_files.append(file)
                else:
                    new_files.append(file)

        for file in previous_hashes:
            if file not in current_hashes:
                deleted_files.append(file)

        if modified_files:
            print("[!] Modified files detected:")
            for file in modified_files:
                print(f"  - {file}")

        if new_files:
            print("[+] New files detected:")
            for file in new_files:
                print(f" - {file}")

        if deleted_files:
            print("[-] Deleted files detected:")
            for file in deleted_files:
                print(f" - {file}")

        if not (modified_files or new_files or deleted_files):
            print("[*] No changes detected.")

        with open(HASH_STORAGE_FILE, "w") as f:
            json.dump(current_hashes, f, indent=4)

        time.sleep(interval)

if __name__ == "__main__":
    directory_to_monitor = input("Enter the directory path to monitor: ")
    scan_directory = int(input("Enter the scan interval (in seconds): "))
    monitor_changes(directory_to_monitor, scan_directory)


        
