"""This file contains the hangman game.

It's based on the files:
- data.py
- functions.py"""

from data import numbers_of_try
from functions import retrieve_scores, retrieve_user_name, choose_a_word
from functions import retrieve_hidden_word, retrieve_letter, save_scores

# scores of the game
SCORES = retrieve_scores()

# name of the player
USER = retrieve_user_name()

# if user do not exist we add him
if USER not in SCORES.keys():
    SCORES[USER] = 0

# when to stop the game
CONTINUE_GAME = "o"

while CONTINUE_GAME != "n":
    print(f"Player {USER}: {SCORES[USER]} points!")
    WORDS_TO_FIND = choose_a_word()
    FIND_LETTER = []
    FIND_WORD = retrieve_hidden_word(WORDS_TO_FIND, FIND_LETTER)
    NUMB_CHANCES = numbers_of_try
    while WORDS_TO_FIND != FIND_WORD and NUMB_CHANCES > 0:
        print(f"(chance {NUMB_CHANCES} left)")
        LETTER = retrieve_letter()
        if LETTER in FIND_LETTER:  # letter already choose
            print("letter already choosen.")
        elif LETTER in WORDS_TO_FIND:  # letter is in the word to find
            FIND_LETTER.append(LETTER)
            print("good game!")
        else:
            NUMB_CHANCES -= 1
            print("try again...")
        FIND_WORD = retrieve_hidden_word(WORDS_TO_FIND, FIND_LETTER)

    # is it game over?
    if WORDS_TO_FIND == FIND_WORD:
        print(f"GG! you find the word {WORDS_TO_FIND}.")
    else:
        print(f"Hangover! You lose.\nThe word to find was:\n{WORDS_TO_FIND}")

    # updated user scores
    SCORES[USER] += NUMB_CHANCES

    CONTINUE_GAME = input("You want to continue (O/N) ?")
    CONTINUE_GAME = CONTINUE_GAME.lower()

# game is over
save_scores(SCORES)

# Display the user scores
print(f"You finished the game with {SCORES[USER]} points.")
