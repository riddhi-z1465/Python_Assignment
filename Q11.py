# Write a function that returns the length of a string without using the built-in len().
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
user_input = input("Enter a string: ")
length = string_length(user_input)
print(f"The length of the string is: {length}")
