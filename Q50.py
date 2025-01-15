# Using the GCD function, write a function lcm(a, b) that returns the least common multiple.
def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Calculate the Least Common Multiple (LCM) of a and b."""
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)
print(f"The Least Common Multiple of {num1} and {num2} is: {result}")