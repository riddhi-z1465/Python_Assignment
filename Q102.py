# Write a function that randomly selects an element from a given list using the random module.
import random

def select_random_element(input_list):
    """Selects a random element from the given list."""
    if not input_list:  # Check if the list is empty
        return None
    return random.choice(input_list)  # Randomly select an element

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    random_element = select_random_element(sample_list)
    print(f"Randomly selected element: {random_element}")