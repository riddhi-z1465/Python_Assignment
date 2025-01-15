# Write a program that lists all files and directories in the current directory using os.listdir().
import os

# Get the current directory
current_directory = os.getcwd()

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)

# Print the current directory
print(f"Listing files and directories in: {current_directory}\n")

# Print each file and directory
for item in files_and_directories:
    print(item)