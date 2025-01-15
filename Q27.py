# Prompt for a string and replace all occurrences of a specific character with another.
original_string = input("Enter the original string: ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")
modified_string = original_string.replace(char_to_replace, replacement_char)
print("The modified string is:", modified_string)