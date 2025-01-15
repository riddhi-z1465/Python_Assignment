# Prompt the user for a number n
n = int(input("Enter a number n: "))
squares_dict = {}

for i in range(1, n + 1):
    squares_dict[i] = i ** 2  

print("Dictionary of squares:", squares_dict)