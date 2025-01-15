# Prompt the user for a number (as a string) and compute the sum of its digits.
number_str = input("Enter a number: ")
sum_of_digits = 0
for char in number_str:
    if char.isdigit():  
        sum_of_digits += int(char) 
print("The sum of the digits is:", sum_of_digits)