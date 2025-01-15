# The program should generate a random number between 1 and 10. The user guesses until they get it right.
import random
random_number = random.randint(1, 10)
guess = None

print("Welcome to the 'Guess the Number' game!")
print("I have selected a number between 1 and 10. Try to guess it!")
while guess != random_number:
    guess = int(input("Enter your guess: "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
