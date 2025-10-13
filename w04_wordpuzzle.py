# Word Puzzle Game - Milestone Submission
# I plan to add hint logic and a random word selector to exceed requirements.

secret_word = "mosiah"
guess_count = 0

print("Welcome to the word guessing game!")

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        print("Your guess was not correct.")