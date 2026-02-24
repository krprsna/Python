# for loop
fruits = ["Apple", "Peach", "Pear"]
for i in fruits:
    print(i) # within the loop
    print(i + " 1 KG") # within the loop
    print(fruits) # within the loop
print(fruits) # outside of the loop
Apple
Apple 1 KG
['Apple', 'Peach', 'Pear']
Peach
Peach 1 KG
['Apple', 'Peach', 'Pear']
Pear
Pear 1 KG
['Apple', 'Peach', 'Pear']
['Apple', 'Peach', 'Pear']



# Find min and max number from the list
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Method 1
max_score = max(student_scores)
min_score = min(student_scores)
print(f"The highest score in the list is '{max_score}' and the lowest score is '{min_score}'")
The highest score in the list is '199' and the lowest score is '24'
# Method 2
student_scores.sort()
print("Highest Score is: " + str(student_scores[-1]))
student_scores.sort(reverse=True)
print("Highest Score is: " + str(student_scores[0]))
Highest Score is: 199
Highest Score is: 199
# Method 3
maxi = 0
for score in student_scores:
     if score > maxi:
         maxi = score
print(f"The Max score is: " + str(maxi))
The Max score is: 199



# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total = 0
for i in range(1, 101):
    total += i
print("Total is: " + str(total))
Total is: 5050



# Fizz Buzz game
///You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for i in range(1, 17):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# Password generator:
Easy Version - Random letter/symbol/number will be displayed in sequence
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_password = '' ## Empty variable
for i in range(nr_letters): ## Getting the range
    random_password += random.choice(letters) ## Appending random let to the variable
for i in range(nr_symbols): ## Getting the range
    random_password += random.choice(symbols) ## Appending random sym to the variable
for i in range(nr_numbers): ## Getting the range
    random_password += random.choice(numbers) ## Appending random num to the variable
print(random_password)
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
4
How many numbers would you like?
4
qqEv!$&!8793

Hard Version - Random letter/symbol/number will be displayed in suffered string
Code:
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_password = '' ## Empty variable
for i in range(nr_letters): ## Getting the range
    random_password += random.choice(letters) ## Appending random let to the variable
for i in range(nr_symbols): ## Getting the range
    random_password += random.choice(symbols) ## Appending random sym to the variable
for i in range(nr_numbers): ## Getting the range
    random_password += random.choice(numbers) ## Appending random num to the variable
str_lst = list(random_password)
random.shuffle(str_lst)
print("".join(str_lst))
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
4
How many numbers would you like?
4
H8b9g!95P++(
