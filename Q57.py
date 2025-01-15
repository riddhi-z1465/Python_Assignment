# Search for a specific word in a file and replace it with another word, then overwrite the file with the changes.
file_path = 'example.txt'

word_to_find = input("Enter the word to find: ")
word_to_replace = input("Enter the word to replace it with: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(word_to_find, word_to_replace)
    with open(file_path, 'w') as file:
        file.write(new_content)

    print(f"Successfully replaced '{word_to_find}' with '{word_to_replace}' in '{file_path}'.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")