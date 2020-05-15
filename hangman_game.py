"""This file contains the hangman game.

It's based on the files:
- data.py
- functions.py"""

from data import numbers_of_try
from functions import retrieve_scores, retrieve_user_name, choose_a_word, retrieve_hidden_word, retrieve_letter, save_scores

# scores of the game
scores = retrieve_scores()

# name of the player
user = retrieve_user_name()

# if user do not exist we add him
if user not in scores.keys():
    scores[user] = 0

# when to stop the game
continue_game = "o"

while continue_game != "n":
    print("Player {0}: {1} points!".format(user, scores[user]))
    words_to_find = choose_a_word()
    find_letters = []
    find_word = retrieve_hidden_word(words_to_find, find_letters)
    numb_chances = numbers_of_try
    while words_to_find != find_word and numb_chances > 0:
        print("Word to find {0} (chance {1} left)".format(words_to_find, numb_chances))
        letter = retrieve_letter()
        if letter in find_letters:  # letter already choose
            print("letter already choosen.")
        elif letter in words_to_find:  # letter is in the word to find
            find_letters.append(letter)
            print("good game!")
        else:
            numb_chances -= 1
            print("try again...")
        find_word = retrieve_hidden_word(words_to_find, find_letters)

    # is it game over?
    if words_to_find == find_word:
        print("GG! you find the word {0}.".format(words_to_find))
    else:
        print("Hangover !!! You lose.")

    # updated user scores
    scores[user] += numb_chances

    continue_game = input("You want to continue (O/N) ?")
    continue_game = continue_game.lower()

# game is over
save_scores(scores)

# Display the user scores
print("you finished the game with {0} points.".format(scores[user]))
