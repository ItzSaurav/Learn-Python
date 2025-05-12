# install an external module and use it to perform an operation of your interest
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
import os

# List files/folders in the current directory
files_and_folders = os.listdir()

# Print each item
print("Files and folders in this directory:")
for item in files_and_folders:
    print(item)