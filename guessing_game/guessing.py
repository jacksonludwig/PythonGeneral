import random

n = random.randint(1, 100)
guess = -1

while guess != n:
    guess = int(input("Enter an integer: "))
    if guess < n:
        print("your guess is too low")
    elif guess > n:
        print("your guess is too high")

print("You guessed correctly")
