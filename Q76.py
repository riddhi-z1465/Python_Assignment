# Write a Python script that reads a text file and prints its contents.
def read_file_contents(filename):
    """Read the contents of the specified file and print them."""
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            contents = file.read()  # Read the entire file contents
            print(contents)  # Print the contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your desired file name
    read_file_contents(filename)