# Implement the bubble sort algorithm to sort a list of numbers in ascending order.
numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, numbers.split()))
n = len(numbers_list)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):

        if numbers_list[j] > numbers_list[j + 1]:
            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
            swapped = True
    if not swapped:
        break
print("Sorted list in ascending order:")
print(numbers_list)