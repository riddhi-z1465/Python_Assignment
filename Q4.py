# Prompt the user for two numbers and display their sum, difference, product, and quotient.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
if operator == '+':
    sum = num1 + num2
    print(f"The result of {num1} + {num2} is: {sum}")
elif operator == '-':
    sub = num1 - num2
    print(f"The result of {num1} - {num2} is: {sub}")
elif operator == '*':
    prod = num1 * num2
    print(f"The result of {num1} * {num2} is: {prod}")
elif operator == '/':
    if num2 != 0:
        div = num1 / num2
        print(f"The result of {num1}/{num2} is: {div}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operator. Please enter one of +, -, *, /,%.")