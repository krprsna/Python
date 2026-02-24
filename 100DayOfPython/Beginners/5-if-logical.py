# Check Odd or Even
get_val = int(input("Enter a number to check if it is even or odd: "))
if get_val % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")



# Ticket price
get_height = int(input("Enter your height in cm: "))
if get_height >= 120:
    print("You can get into the ride.")
    get_age = int(input("Enter your age: "))
    if get_age <= 12:
        print("The ticket is $5")
    elif get_age <=18:
        print("The ticket is $10")
    else:
        print("The ticket is $15")
else:
    print ("You can no get into the ride")



# Ticeket price extended
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is $0.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")



# Pizza price
s_pizza = 15
m_pizza = 20
l_pizza = 25
s_pep = 2
m_l_pep = 3
cheese = 1
if size == "S":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {s_pizza + 2 + 1}")
        else:
            print(f"Your Pizza is: {s_pizza + 2}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {s_pizza + 1}")
        else:
            print(f"Your Pizza is: {s_pizza}")
elif size == "M":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {m_pizza + 3 + 1}")
        else:
            print(f"Your Pizza is: {m_pizza + 3}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {m_pizza + 1}")
        else:
            print(f"Your Pizza is: {m_pizza}")
elif size == "L":
    if pepperoni == "Y":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {l_pizza + 3 + 1}")
        else:
            print(f"Your Pizza is: {l_pizza + 3}")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            print(f"Your Pizza is: {l_pizza + 1}")
        else:
            print(f"Your Pizza is: {l_pizza}")
else:
    print("Enter valid option")


# Treasure game:
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
r_l = input("Left or Right: ")
if r_l.lower() == "right":
    print("Game Over")
elif r_l.lower() == "left":
    s_w = input("Would you like to swim or wait for the boat: ")
    if s_w.lower() == "swim":
        print("Game Over - You have been bitten by Shark")
    elif s_w.lower() == "wait":
        door = input("Choose the door, Red or Yellow or Blue: ")
        if door.lower() == "red":
            print("Game Over - Burned by fire")
        elif door.lower() == "yellow":
            print("You win, you get the treasure")
        elif door.lower() == "blue":
            print("Game Over - Eaten by beasts")
    else:
        print("Enter valid option")
else:
    print("Enter valid option")
