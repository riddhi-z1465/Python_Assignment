# Read a file and count how many lines it contains.
file_path = 'example.txt'  # Change this to your file path

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Initialize a line counter
        line_count = 0
        
        # Iterate through each line in the file
        for line in file:
            line_count += 1  # Increment the line counter for each line

    # Print the total number of lines
    print(f"The file '{file_path}' contains {line_count} lines.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")