# Given a list of integers, prompt for a specific integer and count how many times it appears.
numbers = [1, 2, 3, 2, 4, 2, 5, 3, 1]  
target = int(input("Enter an integer to count its occurrences: "))

count = 0
for num in numbers:
    if num == target:
        count += 1  
print(f"The integer {target} appears {count} times in the list.")