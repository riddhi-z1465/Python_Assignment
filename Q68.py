# Write a recursive function power(base, exp) that computes base^exp.
def power(base, exp):
    """Compute base raised to the power of exp using recursion."""
    if exp == 0:
        return 1
    # If exp is negative, compute the positive exponent and take the reciprocal
    elif exp < 0:
        return 1 / power(base, -exp)
    # Recursive case: multiply base by the result of power(base, exp - 1)
    else:
        return base * power(base, exp - 1)

# Example usage
if __name__ == "__main__":
    base = float(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    result = power(base, exp)
    print(f"{base} raised to the power of {exp} is: {result}")