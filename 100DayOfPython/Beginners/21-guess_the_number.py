# Method 1
from random import randint
random_num = randint(1, 100)

def hard():
    life = 5
    game_over = True
    while game_over:
        get_user_input = int(input("\nEnter a number to guess: "))
        if get_user_input == random_num:
            print("Correct!")
            game_over = False
        elif get_user_input > random_num:
            print("Too high!")
            life -= 1
            print("Your have only " + str(life) + " guesses left")
        elif get_user_input < random_num:
            print("Too low!")
            life -= 1
            print("Your have only " + str(life) + " guesses left")
        else:
            print("Wrong Input!")
        if life == 0:
            print("Game Over")
            game_over = False

def easy():
    life = 10
    game_over = True
    while game_over:
        get_user_input = int(input("\nEnter a number to guess: "))
        if get_user_input == random_num:
            print("Correct!")
            game_over = False
        elif get_user_input > random_num:
            print("Too high!")
            life -= 1
            print("Your have only " + str(life) + " guesses left")
        elif get_user_input < random_num:
            print("Too low!")
            life -= 1
            print("Your have only " + str(life) + " guesses left")
        else:
            print("Wrong Input!")
        if life == 0:
            print("Game Over")
            game_over = False

difficulty = input("\nChoose the difficulty of 'hard' or 'easy': ").lower()
if difficulty == "hard":
    hard()
elif difficulty == "easy":
    easy()
else:
    print("\nEnter valid data...")
