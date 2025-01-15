# Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only odd numbers (filter out even numbers)
filtered_numbers = filter(lambda x: x % 2 != 0, numbers)

# Use reduce to sum the filtered numbers
sum_of_filtered = reduce(lambda x, y: x + y, filtered_numbers)
print(f"The sum of the filtered (odd) numbers is: {sum_of_filtered}")