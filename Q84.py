# Write a program that appends a user-input line to an existing file without overwriting it.
def append_to_file(filename, line):
    """Append a line to the specified file."""
    with open(filename, mode='a') as file:  # Open the file in append mode
        file.write(line + '\n')  # Write the line followed by a newline

# Example usage
if __name__ == "__main__":
    # Specify the filename
    filename = 'example.txt'  # Replace with your desired file name

    # Get user input
    user_input = input("Enter a line to append to the file: ")

    # Append the user input to the file
    append_to_file(filename, user_input)

    print(f"The line has been appended to '{filename}'.")