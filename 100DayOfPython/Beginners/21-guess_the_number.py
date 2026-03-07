# Method 1
import random
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
random_num = random.choice(number)
print(random_num)

def hard():
    life = 5
    game_over = True
    while game_over:
        get_user_input = input("\nEnter a number to guess: ")
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
        get_user_input = input("\nEnter a number to guess: ")
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
