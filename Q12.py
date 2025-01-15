# Write a program that checks if a given string is a palindrome.
input_string = input("Enter a string: ")
input_string = input_string.lower()

input_string = input_string.replace(" ", "")
if input_string == input_string[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")