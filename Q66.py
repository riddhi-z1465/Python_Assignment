# Implement a function factorial(n) that calculates n! using recursion.
def factorial(n):
    """Return the factorial of n using recursion."""
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer to compute its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")