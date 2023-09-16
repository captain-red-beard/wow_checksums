import hashlib
import os
import argparse
import json
import re

def compute_sha256(file_path):
    """Compute the SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        # Read the file in small chunks until EOF
        chunk = file.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = file.read(4096)
    return hasher.hexdigest()

def hash_all_files_in_directory(directory):
    """Compute the SHA256 hash of all files in a directory (recursively)."""
    file_hashes = {}
    for foldername, subfolders, filenames in os.walk(directory):
        relative_root = os.path.relpath(foldername, directory)
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            relative_file_path = os.path.join(relative_root, filename)
            relative_file_path = relative_file_path.replace("\\", "/")
            relative_file_path = re.sub(r'\./', '', relative_file_path)
            file_hashes[relative_file_path] = compute_sha256(file_path)

    combined_hashes = ''.join(file_hashes.values())
    final_hash = hashlib.sha256(combined_hashes.encode()).hexdigest()

    return {
        'name': directory,
        'hash': final_hash,
        'files': file_hashes
    }


def main():
    parser = argparse.ArgumentParser(description="A simple CLI application with options and flags.")
    parser.add_argument('--version', type=str, help="Version to compare checksums to.")
    parser.add_argument('--verbose', '-v', type=bool)
    parser.add_argument('directory', type=str, help="Directory who's checksums to check")
    args = parser.parse_args()
    
    verbose = args.verbose
    dir_path = args.directory

    if not os.path.exists(dir_path) and os.path.isdir(dir_path):
        raise("Invalid directory path.")

    results = hash_all_files_in_directory(dir_path)


    with open("./result.json", "w") as file:
        json.dump(results, file, indent=4)


main()