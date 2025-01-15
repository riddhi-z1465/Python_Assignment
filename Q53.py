# Copy the contents of one text file to another.
# Specify the source and destination file paths
source_file_path = 'source.txt'  # Change this to your source file path
destination_file_path = 'destination.txt'  # Change this to your destination file path

try:
    # Open the source file in read mode
    with open(source_file_path, 'r') as source_file:
        # Read the content of the source file
        content = source_file.read()

    # Open the destination file in write mode
    with open(destination_file_path, 'w') as destination_file:
        # Write the content to the destination file
        destination_file.write(content)

    print(f"Contents copied from '{source_file_path}' to '{destination_file_path}'.")

except FileNotFoundError:
    print(f"Error: The file '{source_file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")