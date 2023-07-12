'''This script will search for files recursively in a provided directory and its sub directories and provide the file path if it matches
For example if you want to search for a file name called test.txt in /home/user/ directory. You can use the script 
that will search in all the sub directories and print the file path
'''

import os
import argparse

def find(directory, search_term, recursive=False):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_term in file:
                print(os.path.join(root, file))

        if not recursive:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for files in a directory.")
    parser.add_argument("-d", "--directory", help="The directory to search in.", required=True)
    parser.add_argument("-m", "--search_term", help="The term to search for in filenames.", required=True)
    parser.add_argument("-r", "--recursive", action="store_true", help="Perform a recursive search.")

    args = parser.parse_args()

    find(args.directory, args.search_term, args.recursive)