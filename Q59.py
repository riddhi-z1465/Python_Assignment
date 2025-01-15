# Write a script that takes command-line arguments (e.g., file paths) and prints them.
import sys
if len(sys.argv) > 1:
    print("Command-line arguments:")
    for arg in sys.argv[1:]: 
        print(arg)
else:
    print("No command-line arguments provided.")