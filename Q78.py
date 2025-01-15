# Write a Python program to copy the contents of one file to another.
def copy_file_contents(source_filename, destination_filename):
    """Copy the contents of the source file to the destination file."""
    try:
        with open(source_filename, 'r') as source_file:
            with open(destination_filename, 'w') as destination_file:
                for line in source_file:
                    destination_file.write(line)  # Write each line to the destination file
        print(f"Contents copied from '{source_filename}' to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source_filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while copying the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    source_filename = 'source.txt'  # Replace with your source file name
    destination_filename = 'destination.txt'  # Replace with your destination file name
    copy_file_contents(source_filename, destination_filename)