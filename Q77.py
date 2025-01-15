# Write a program that prompts the user for a line of text and writes that line to a file.
def write_line_to_file(filename, line):
    """Write the given line to the specified file."""
    with open(filename, 'w') as file:  # Open the file in write mode
        file.write(line + '\n')  # Write the line followed by a newline

if __name__ == "__main__":
    filename = 'output.txt'  # Replace with your desired file name
    user_input = input("Please enter a line of text: ")  # Prompt user for input
    write_line_to_file(filename, user_input)  # Write the input to the file
    print(f"The line has been written to '{filename}'.")