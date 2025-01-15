# Implement a function recursive_sum(lst) that sums all elements in a list using recursion.
def recursive_sum(lst):
    """Calculate the sum of a list using recursion."""
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    else:
        # Recursive case: return the first element plus the sum of the rest of the list
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]  
result = recursive_sum(numbers)
print(f"The sum of the list {numbers} is: {result}")