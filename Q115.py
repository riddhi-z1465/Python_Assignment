# Write a simple decorator timer that measures the execution time of a function.
import time

def timer(func):
    """A simple decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time before function execution
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # End time after function execution
        print(f"Execution time: {end_time - start_time:.4f} seconds")  # Print execution time
        return result  # Return the result of the original function
    return wrapper

# Example usage
@timer
def example_function(n):
    """A function that sums numbers from 0 to n."""
    total = sum(range(n))  # Sum numbers from 0 to n
    return total

if __name__ == "__main__":
    result = example_function(1000000)  # Call the decorated function
    print(f"Result: {result}")  # Print the result