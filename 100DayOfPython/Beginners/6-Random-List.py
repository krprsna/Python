# Heads or Tails :
import random
head_tail = random.randrange(0, 2)
if head_tail == 0:
    print("Heads")
elif head_tail == 1:
    print("Tails")
else:
    print("Invalid option")



# List:
fruits = ["Apple", "Orangeee", "Cherry", "Banana"]
print(fruits)
['Apple', 'Orangeee', 'Cherry', 'Banana']
print(fruits[2]) # Indexing
Cherry
fruits[1] = "Orange" # Rename
print(fruits[1])
Orange
fruits.append("Mango") # Append
print(fruits)
['Apple', 'Orange', 'Cherry', 'Banana', 'Mango']
fruits.remove("Cherry") # Remove
print(fruits)
['Apple', 'Orange', 'Banana', 'Mango']
fruits.sort() # Sort Alphabatical
print(fruits)
['Apple', 'Banana', 'Mango', 'Orange']
fruits.reverse() # Sort Reverse 
print(fruits)
['Orange', 'Mango', 'Banana', 'Apple']
fruits.pop() # Remove the last index
print(fruits)
['Apple', 'Banana', 'Mango']



# Random:
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))



# List with index
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"] 
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables] # This is also considered as individual list, but each list contains the data present in the above list
print(dirty_dozen[1][1]) # Index 1 of 1
Kale



# Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = input("Enter Rock, Paper, or Scissors: ").upper()
computer_random = random.choice(["Rock", "Paper", "Scissors"]).upper()
if user_input == "ROCK":
    print(rock)
    if computer_random == "ROCK":
        print(rock)
        print("Tie")
    elif computer_random == "PAPER":
        print(paper)
        print("You Win")
    elif computer_random == "SCISSORS":
        print(scissors)
        print("You Lose")
elif user_input == "PAPER":
    print(paper)
    if computer_random == "PAPER":
        print(paper)
        print("Tie")
    elif computer_random == "ROCK":
        print(rock)
        print("You Win")
    elif computer_random == "SCISSORS":
        print(scissors)
        print("You Lose")
elif user_input == "SCISSORS":
    print(scissors)
    if computer_random == "SCISSORS":
        print(scissors)
        print("Tie")
    elif computer_random == "PAPER":
        print(paper)
        print("You Win")
    elif computer_random == "ROCK":
        print(rock)
        print("You Lose")
else:
    print("Invalid Input")
