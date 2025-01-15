# Write a script that uses the math module to compute the square root, floor, and ceiling of a user-input number.
import math

# Get user input
user_input = input("Enter a number: ")

try:
    # Convert input to a float
    number = float(user_input)

    # Compute square root
    square_root = math.sqrt(number)

    # Compute floor
    floor_value = math.floor(number)

    # Compute ceiling
    ceiling_value = math.ceil(number)

    # Print the results
    print(f"Number: {number}")
    print(f"Square Root: {square_root}")
    print(f"Floor: {floor_value}")
    print(f"Ceiling: {ceiling_value}")

except ValueError:
    print("Please enter a valid number.")