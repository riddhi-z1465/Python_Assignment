# Write a recursive function that computes the sum of all elements in a list.
def sum_of_list(lst):
    """Compute the sum of all elements in a list using recursion."""

    if not lst:
        return 0
    # Recursive case: return the first element plus the sum of the rest of the list
    return lst[0] + sum_of_list(lst[1:])

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5] 
    total_sum = sum_of_list(numbers)
    print(f"The sum of the list is: {total_sum}")