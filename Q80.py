# Write a program that counts how many lines are in a file.
def count_lines_in_file(filename):
    """Count the number of lines in the specified file and print the count."""
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)  # Count lines using a generator expression
        print(f"The file '{filename}' contains {line_count} lines.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file name
    count_lines_in_file(filename)