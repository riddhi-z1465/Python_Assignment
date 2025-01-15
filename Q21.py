# Find the minimum and maximum values in a list without using built-in min() or max().
numbers = [10, 20, 5, 40, 15] 

if numbers:  
    min_value = numbers[0]
    max_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num  
        if num > max_value:
            max_value = num  
    print("The minimum value in the list is:", min_value)
    print("The maximum value in the list is:", max_value)
else:
    print("The list is empty.")