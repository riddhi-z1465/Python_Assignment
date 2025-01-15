# Write a program that swaps the values of two variables without using a temporary variable.
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
