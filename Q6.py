# Prompt the user for an integer and print whether it’s even or odd.
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
