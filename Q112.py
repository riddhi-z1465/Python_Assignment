# Use a lambda function inside map to transform a list of numbers (e.g., multiply each by 2).
numbers = [1, 2, 3, 4, 5]

# Use map with a lambda function to multiply each number by 2
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the result
print(f"The original numbers: {numbers}")
print(f"The doubled numbers: {doubled_numbers}")