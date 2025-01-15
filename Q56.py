# Write a function that attempts to convert a string to an integer, catching any ValueError and printing a custom message.
user_input = input("Enter a string to convert to an integer: ")

try:
    # Attempt to convert the string to an integer
    result = int(user_input)
    print(f"The converted integer is: {result}")
except ValueError:
    # Catch ValueError and print a custom message
    print("Error: The provided input is not a valid integer.")