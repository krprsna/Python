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



# Method 2
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

