# Find the second largest element in a list of unique integers.
# Example list of unique integers
numbers = [10, 20, 4, 45, 99]

if len(numbers) < 2:
    print("The list must contain at least two unique integers.")
else:
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1]
    print("The second largest element is:", second_largest)