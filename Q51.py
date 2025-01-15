# Write a program that reads a text file and prints its contents to the screen.
file_path = 'example.txt'  # Change this to your file path

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Print the contents to the screen
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")