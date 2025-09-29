# Word Puzzle Game - Final Version
# Added hint logic and guess length validation. Also added random word selection for creativity. 

import random
# 🎨 Creative Enchancement:

# The game randomly selects a secret word from a list to make each playthrough unique.

word_list = ["Mosia", "temple", "moroni", "helaman", "nephi"]
secret_word = random.choice(word_list)
guess_count = 0

print("Welcome to the word guessing game!")
print("Your hint is:", "_"*len(secret_word))

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    if guess == secret_word:
        print("Congratulations! You've guessed it!")
        print(f"It took you {guess_count} guesses.")
        break

    # Generate hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() = ""
        elif guess[i] in secret_word:
            hint += guess[i].lower() + ""
    
        else:
            hint += "_"
        print("Your hint is:", hint.strip())
