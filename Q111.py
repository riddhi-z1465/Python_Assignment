# Demonstrate advanced list slicing (e.g., reversing a list with slicing, skipping elements) in a script.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Reversing a list using slicing
reversed_numbers = numbers[::-1]
print(f"Original list: {numbers}")
print(f"Reversed list: {reversed_numbers}")

# 2. Skipping elements in a list
# Skipping every second element (taking every second element)
skipped_numbers = numbers[::2]
print(f"Every second element: {skipped_numbers}")

# 3. Reversing a list and skipping elements
# Reversing the list and taking every second element
reversed_skipped_numbers = numbers[::-2]
print(f"Reversed list with every second element: {reversed_skipped_numbers}")

# 4. Slicing a specific range
# Getting elements from index 2 to 7 (exclusive)
sliced_range = numbers[2:7]
print(f"Elements from index 2 to 7: {sliced_range}")

# 5. Slicing with negative indices
# Getting the last three elements
last_three = numbers[-3:]
print(f"Last three elements: {last_three}")