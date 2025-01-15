# Prompt for principal, rate, and time to calculate compound interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + (rate / (100 * n))) ** (n * time)
compound_interest = amount - principal

print(f"The compound interest is {compound_interest:.2f}.")
print(f"The total amount after {time} years is {amount:.2f}.")
