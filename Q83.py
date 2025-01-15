# Write a program to search for a specific substring in a file and print the lines where it appears.
def search_in_file(filename, substring):
    """Search for a substring in the specified file and print the lines where it appears."""
    try:
        with open(filename, 'r') as file:
            found = False
            for line_number, line in enumerate(file, start=1):
                if substring in line:
                    print(f"Line {line_number}: {line.strip()}")
                    found = True
            if not found:
                print(f"The substring '{substring}' was not found in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file name
    substring = input("Enter the substring to search for: ")
    search_in_file(filename, substring)
