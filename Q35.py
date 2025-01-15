# Check if a number is a palindrome (e.g., 121 → palindrome).
number = input("Enter a number to check if it is a palindrome: ")
if number == number[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")