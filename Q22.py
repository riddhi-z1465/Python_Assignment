# Reverse a list in-place (without using reversed() or slicing).
numbers = [1, 2, 3, 4, 5]  

left = 0  
right = len(numbers) - 1  

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1
print("Reversed list:", numbers)