secret_word = "dog"
guess = ""
guess_count = 0
guess_limit = 5

while(guess != secret_word and guess_count < guess_limit):
    guess = input("Try to guess the secret word: ")
    guess_count += 1

if guess == secret_word:
    print("You found the secret word")
else:
    print("You ran out of guesses")
