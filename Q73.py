# Write a recursive function that takes a list which may contain nested lists and returns a flat list of all elements.
def flatten(nested_list):
    """Flatten a nested list into a single list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, recursively flatten it
            flat_list.extend(flatten(item))
        else:
            # If the item is not a list, add it to the flat list
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    nested_list = [1, [2, 3, [4, 5]], 6, [7, 8], 9]
    flat_list = flatten(nested_list)
    print("Flattened list:", flat_list)