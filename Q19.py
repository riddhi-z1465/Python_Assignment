# Prompt the user for 5 integers and store them in a list. Print the list and its length.
numbers = []
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: ")) 
    numbers.append(num)  
print("The list of integers is:", numbers)
print("The length of the list is:", len(numbers))