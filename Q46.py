# Count how often each element appears in a list and store the result in a dictionary.
elements = [1, 2, 2, 3, 4, 4, 4, 5]

# Initialize an empty dictionary to store frequencies
frequency_dict = {}
for element in elements:
    if element in frequency_dict:
        frequency_dict[element] += 1  # Increment the count if the element is already in the dictionary
    else:
        frequency_dict[element] = 1  

# Print the frequency of each element
print("Frequency of elements:")
for element, count in frequency_dict.items():
    print(f"{element}: {count}")