# Implement a function fib(n) to return the nth Fibonacci number using recursion.
def fib(n):
    """Return the nth Fibonacci number using recursion."""
    # Base cases
    if n <= 0:
        return 0  # Fibonacci of 0 is 0
    elif n == 1:
        return 1  # Fibonacci of 1 is 1
    # Recursive case: sum of the two preceding numbers
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the position of the Fibonacci number to compute: "))
    result = fib(n)
    print(f"The {n}th Fibonacci number is: {result}")