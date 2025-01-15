# Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.
def gcd(a, b):
    """Compute the GCD of two numbers using recursion."""
    if b == 0:
        return a  # Base case: if b is 0, GCD is a
    else:
        return gcd(b, a % b)  # Recursive case
if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")