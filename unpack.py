"""
For semantica to work I need all notes to be in the same folder `notes/`.
This is the script I use to "unpack" all markdown nodes when nested inside sub-directories. 
Run this script inside the notes directory to extract all notes from sub-directories and move them to the current directory.
"""
import os
import shutil

def move_markdown_files_to_root(root_dir):
    # Walk through all subdirectories in the root directory
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Skip the root directory itself
        if foldername == root_dir:
            continue
        
        # Iterate through each file in the subdirectory
        for filename in filenames:
            # Check if the file has a markdown extension
            if filename.endswith(".md"):
                # Construct full file path
                file_path = os.path.join(foldername, filename)
                # Move the file to the root directory
                shutil.move(file_path, os.path.join(root_dir, filename))
                print(f"Moved {filename} to {root_dir}")

if __name__ == "__main__":
    root_directory = "."

    choice = input("This script will move all markdown files from the sub-directories of the current directory to the root of this directory. Continue? [yN]") 

    if(choice.lower == "y"):
        move_markdown_files_to_root(root_directory)
    else:
        exit("Aborting.")