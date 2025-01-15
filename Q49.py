# Implement the Euclidean algorithm to find the greatest common divisor of two numbers.
def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b  # Update a and b
    return abs(a)  # Return the absolute value of GCD
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The Greatest Common Divisor of {num1} and {num2} is: {result}")