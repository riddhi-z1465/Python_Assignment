# Given a dictionary, invert it (keys become values, values become keys).
original_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# Initialize an empty dictionary for the inverted result
inverted_dict = {}

# Invert the dictionary
for key, value in original_dict.items():
    inverted_dict[value] = key  # Set the value as the key and the key as the value

# Print the original and inverted dictionaries
print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_dict)