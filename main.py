# Hangman Game

import random
import hangman_art
import hangman_words

# Print the ASCII art for logo of hangman.
print(hangman_art.logo)

# Randomly choosing a word from the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Creating a list of blanks for the chosen word.
display = []
for _ in range(word_length):
    display += "_"

# While the game hasn't ended:
while not end_of_game:

    # Input a single character.
    guess = input("Guess a letter: ").lower()

    # If the user has already guessed that character, let them know.
    if guess in display:
        print("You've already guessed this letter!")

    # Check if guessed alphabet is in the word.
    # If yes, then put it in the display list [the list with blanks].
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user has guessed wrong alphabet.
    # If yes, then let them know, and reduce a life.
    # If no of lives = 0, then end the game.
    if guess not in chosen_word:
        print("'" + guess + "'" + " is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word was: {chosen_word}")

    # Join all the alphabets in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # Check if user has got all letters, end the game.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the ASCII art for stages of hangman.
    print(hangman_art.stages[lives])