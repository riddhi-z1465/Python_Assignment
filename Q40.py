# Write an iterative binary search function to find an element in a sorted list.
def binary_search(sorted_list, target):
    """Perform an iterative binary search on a sorted list."""
    left, right = 0, len(sorted_list) - 1  

    while left <= right:
        mid = (left + right) // 2  
        if sorted_list[mid] == target:
            return mid  
        elif sorted_list[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the list.")