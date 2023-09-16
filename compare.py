import hashlib
import os
import argparse
import json



def main():
    parser = argparse.ArgumentParser(description="A simple CLI application with options and flags.")
    parser.add_argument('--verbose', '-v', type=bool)
    parser.add_argument('version', type=str, help="Version to compare checksums to.")
    args = parser.parse_args()
    
    verbose = args.verbose
    version = args.version

    if not os.path.exists(dir_path) and os.path.isdir(dir_path):
        raise("Invalid directory path.")

    results = hash_all_files_in_directory(dir_path)


    with open("./result.json", "w") as file:
        json.dump(results, file, indent=4)


main()