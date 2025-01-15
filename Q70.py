# Implement binary search recursively to find an element in a sorted list.
def binary_search(arr, target, low, high):
    """Perform a recursive binary search on a sorted list."""
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2  # Find the middle index

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid  # Target found, return the index
    elif arr[mid] < target:
        # Target is in the right half
        return binary_search(arr, target, mid + 1, high)
    else:
        # Target is in the left half
        return binary_search(arr, target, target, mid - 1)

# Example usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = int(input("Enter the number to search for: "))
    result = binary_search(sorted_list, target, 0, len(sorted_list) - 1)

    if result != -1:
        print(f"Element {target} found at index: {result}")
    else:
        print(f"Element {target} not found in the list.")