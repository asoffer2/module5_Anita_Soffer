"""""
1. Import random
2. define ask_choice and check_letter
   to accept only allowed user input and prompt and 
   retry otherwise, ignoring and reprompting blank input
3. make an outer while loop for a new game. 
   a) create lists: 
      words lists (3 categories), revealed_letters, guessed_letters
4. Set correct_letters, wins, losses, tries, total_correct_letters
    = 0, 
5. define word_game:
   a) Add tries based on difficulty level
   b) Choose a random word(curr_word) from the category list chosen. 
   c) For each letter in the word, add an underscore to
      revealed_letters list. 
   d) Prompt for a letter using check_letter function
   e) Set correct_letters at 0
   f)use a for loop to go through each letter in curr_word: 
     I) If the user's letter was equal to the letter of the 
       same index in curr_word, replace the underscore with 
       the user's letter. Add one to correct_letter 
    II) Else, continue
  g) When the loop ends (went through every letter of the word)
     I) If correct_letters was >= 1, add to guessed_letters, add
      one to wins and total_correct_letters, print required
      message (revealed_letters, remaining tries, and guessed_letters),
      and continue the loop to get another letter
      -within this if statement, if there are no underscores left
       in revealed_letters (full letter guessed), print a congrats 
       message, break out of inner and outer while loop. 
      - if full word not guessed (else), tries +=1 and print revealed_letters, 
        remaining tries, and guessed_letters, and continue inner while loop.
  h) Upon exiting the loop:
    - If correct_letters is 0 - the round that was exited on was an incorrect guess
      so print a losing message.
     -Either way, prompt the user to play again/not:
     -If the user wants to play again, call main. If not, exit the function.
6. Define main:
   a) Print welcome message, instructions and rules
   b) Prompt for difficulty level and category using ask_choice
   c) Call the word game, passing in arguements
   d) Call main

"""""

import random
from os import WCONTINUED


def ask_choice(prompt, allowed):
    """ Asks for, lowercase and validate string type
        user input and makes sure it is withing the
        allowed set. """

    allowed_lower = [a.lower() for a in allowed] # lowercase the allowed list
    prompt = prompt + str(allowed_lower) + str(" ") # format 'prompt' to print all three

    while True:
        user_input = input(prompt).lower()
        if user_input not in allowed_lower or user_input == "":
            print("Please enter a value in the set, and no blank spaces.")
            continue
        else:
            return user_input


def check_letter(guessed_letters):
    """ Prompts for, validates, and returns a user's
        valid letter (from a-z)"""

    while True:
        user_input = input("Please enter a single letter: ")
        user_input_fixed = user_input.lower().strip()
        if len(user_input_fixed) > 1 or user_input_fixed == "": # making sure it is a single letter
            print("Please enter only one letter and no spaces")
            continue
        if not user_input_fixed.isalpha(): # letter not number/character
            print("Please enter a letter")
            continue
        if user_input_fixed in guessed_letters:
            print("Letter already guessed. Please choose another one.")
            continue # reprompt repeat guessed
        else:
            return user_input_fixed


def word_game(difficulty_level, category):
    """ A word guessing game, choosing a random word and looping
        until user runs out of tries or guesses the full word."""

    tries = 0 # game begins at 0 tries
    animals_list = ["tiger", "giraffe", "penguin", "dolphin", "zebra",
                    "lion", "eagle", "monkey", "turtle", "spider"]
    food_list = ["apple", "cake", "chicken", "strawberries", "bread",
                 "yogurt", "potatoes", "almonds", "spinach", "chocolate"]
    colors_list = ["red", "blue", "green", "yellow", "pink", "purple",
                   "magenta", "turquoise", "cyan", "white", "indigo"]

    while tries <= 10:  # outer loop starts a new game
        revealed_letters = []
        guessed_letters = []
        correct_letters = 0
        wins = 0
        losses = 0
        total_correct_letters = 0
        if difficulty_level == "med":
            tries = tries + 2  # starts off with 8 tries
        elif difficulty_level == "hard":
            tries = tries + 4  # starts off with 6 tries
        # word choice based on chosen category
        if category == "animals":
            curr_word = random.choice(animals_list)
        elif category == "food":
            curr_word = random.choice(food_list)
        else:
            curr_word = random.choice(colors_list)
        for _ in range(len(curr_word)):  # adding underscores for each letter in the word
            revealed_letters.append("_")
        while tries < 10:  # this loop gets a (new) letter
            print()
            print()
            user_guess = check_letter(
                guessed_letters)  # prompts repeatedly if the user's guess is in the list guessed_letters
            correct_letters = 0
            for i in range(len(curr_word)):  # each letter must be tested through the entire word
                letter = curr_word[i] # a way to access the actual letter at the current index in curr_word
                if user_guess == letter:
                    revealed_letters[i] = user_guess # replacing the _ at the current index with the user's guess
                    correct_letters += 1
                    continue  # possible duplicates
                else:
                    continue  # guessed letter could be later
            if correct_letters >= 1: # letter was in the word at least once
                guessed_letters.append(user_guess)
                wins += 1 # user guessed correctly
                # correct_letters will add extra if there is a double letter so new value for tracking the total
                total_correct_letters += 1
                print(f"Your word so far: {" ".join(revealed_letters)}. Remaining tries: {10 - tries}. Guessed letters: {guessed_letters}")
                if "_" not in revealed_letters: # entire word guessed
                    print()
                    print("''''''''''''''''''''''''''''''")
                    print("------------------------------")
                    print(">>><<<<<<>>>>>>>>><<<<<<<<>>>><")
                    print("<<<Congratulations, you won!>>>")
                    print("<<<<>>>><<<<>>>><<<<>>>><<<<>>>")
                    print("-------------------------------")
                    print("'''''''''''''''''''''''''''''''")
                    print()
                    print(f"Score: {abs(wins - losses)} Wins: {wins} Losses: {losses}")
                    break  # breaks out of inner loop, moves to outermost loop
                else:
                    continue
            else:
                losses += 1
                tries = tries + 1
                guessed_letters.append(user_guess)
                print(
                    f"Your word so far: {" ".join(revealed_letters)}. Remaining tries: {10 - tries}. Guessed letters: {guessed_letters}")
                continue
        break # breaks out of game loop

    if correct_letters == 0:  # ran out of tries
        print()
        print(";;;;;;;;;;;;;;;;;;;;;;;;")
        print("----Sorry, you lost----")
        print(";;;;;;;;;;;;;;;;;;;;;;;;")
    print()
    print()
    again_choice = ask_choice("Do you want to play again?", ["y", "n"]) # runs either way (win/lose)
    if again_choice == "y":
        print()
        print()
        main()
    else:
        return


def main():
    """Printing rules and instructions, and running the main program."""
    
    # UX
    print()
    print("------------------------------------------------")
    print("-------------Welcome To WordGuess!--------------")
    print("------------------------------------------------")
    print()
    print("Instructions:")
    print("1) Choose a difficulty level: you will have 6 tries for hard, 8 for med, and 10 for easy.")
    print("2) Choose a word category")
    print("3) Guess a single letter until you run out of tries!")
    print()
    print("Rules:")
    print("1) Repeats will be ignored and reprompted")
    print("2) A correct guess will not count as a try")
    print("3) Game will end when player runs out of tries or guesses the complete word")
    print("4) Score is calculated by weighing the player's correctly guessed letters against incorrect guesses")
    print()
    print("Good Luck!")
    print()
    difficulty_level = ask_choice("Choose difficulty level", ["easy", "med", "hard"])
    print()
    category = ask_choice("Choose category", ["animals", "food", "color"])

    word_game(difficulty_level, category)


if __name__ == "__main__":
    main()