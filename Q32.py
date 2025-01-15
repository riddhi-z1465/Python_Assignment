# Print the first n Fibonacci numbers using iteration.
n = int(input("Enter the number : "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')  
        a, b = b, a + b  

    print()  