"""This files defined the necessary functions to run the hangman games"""
import os
import pickle
import time
import random
from data import my_scores_file, words_list

# score management


def retrieve_scores():
    """This function store the scores in a dictionary"""

    if os.path.exists(my_scores_file):  # folder exist
        scores_file = open(my_scores_file, "rb")
        depickler = pickle.Unpickler(scores_file)
        scores = depickler.load()
        scores_file.close()
    else:
        scores = {}
    return scores


def save_scores(scores):
    """ This function is in charge to save scores in my_scores_file"""

    scores_file = open(my_scores_file, "wb")  # On écrase les anciens scores
    pickler = pickle.Pickler(scores_file)
    pickler.dump(scores)
    scores_file.close()


# user's inputs


def retrieve_user_name():
    """This function must retrieve the name of the user.
    the name must contient at minimum 4 characters, letters and numbers exclusively """

    user_name = input("What is your name? ")
    # fisrt lettre in capital and the others in lower case
    user_name = user_name.capitalize()
    if not user_name.isalnum() or len(user_name) < 4:
        print("Invalid name")
        # we call the function again
        return retrieve_user_name()
    print("Hello,.{} \nTime to play hangman!".format(user_name))
    time.sleep(1)
    return user_name


def retrieve_letter():
    """This function catch the letter given by the user.
     If it's not a letter we call the function back"""

    letter = input("Chose a letter: ")
    letter = letter.lower()
    if len(letter) > 1 or not letter.isalpha():
        print("You don't enter a correct input.")
        return retrieve_letter
    print("Let's see...")
    time.sleep(1)
    return letter


# game function


def choose_a_word():
    """This function returns the word chossen in the words_to_find list"""

    return random.choice(words_list)


def retrieve_hidden_word(full_word, found_letter):
    """This function returns a hidden word.
    The hidden letters are marked with an asterisk *."""

    hidden_word = ""
    for letter in full_word:
        if letter in found_letter:
            hidden_word += letter
        else:
            hidden_word += "*"
    return hidden_word
