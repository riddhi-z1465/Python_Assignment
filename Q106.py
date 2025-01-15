# Write a script that takes command-line arguments and prints them.
import sys

# Print the name of the script
print("Script name:", sys.argv[0])

# Print the number of command-line arguments
print("Number of arguments:", len(sys.argv) - 1)  # Subtract 1 for the script name

# Print each command-line argument
print("Arguments:")
for i, arg in enumerate(sys.argv[1:], start=1):  # Start from 1 to skip the script name
    print(f"Argument {i}: {arg}")