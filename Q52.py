# Prompt the user for a string and write it to a new text file.
# Prompt the user for a string
user_input = input("Enter a string to write to a file: ")

# Specify the name of the new text file
file_path = 'output.txt'  # Change this to your desired file name

try:
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the user's input to the file
        file.write(user_input)

    print(f"The string has been written to '{file_path}'.")

except Exception as e:
    print(f"An error occurred: {e}")