# Base code
import random
word_list = ["aardvark", "baboon", "camel"]
## Print random word
chosen_word = random.choice(word_list)
print(chosen_word)
# Keep the _ as per the length of the random word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
game_over = False # Setting condition for while loop
store_data = [] # empty list
while not game_over: 
    guess = input("Guess a letter: ").lower()
    display = "" # empty string
    for i in chosen_word: 
        if i == guess: # validating if the guessed word is present in chosen_word
            display += i # if present, add them to the display
            store_data.append(i) # also append them to the list present out of while loop
        elif i in store_data: # ensure to keep the previously guessed world in display
            display += i
        else:
            display += "_" # if the guessed letter is not matched, print _
    print(display)
    if "_" not in display: # when there is no _ present in the display (all the letters guessed)
        game_over = True # Game ends and while loop ends
        print("You Win")



# Hangman full game:
import random
from random import lognormvariate
from hangman_words import word_list # hangman_words is a python code which has all the words
from hangman_art import stages, logo # hangman_art is a python code which has the hangman art

lives = 6
chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"****************************<{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("The letter entered is already guessed - your life retained")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        print("The entered letter is not in the word, you lost a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word} - YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives])
