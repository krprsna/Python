# Indexing
print(len("Hello"))
5
print("Hello"[0])
H
print("Hello"[-1])
o


# Int
print(123, 345)
123 345
print(123 + 345)
468
print(10_00_000) # Printing 10L
1000000


# Float
print(3.14)
3.14


# Boolean
True or False


# Type checking:
print(len("12345")) # This is string, not integer because of the double quotes
5
print(type(12345))
<class 'int'>
print(type("12345"))
<class 'str'>
print(type(3.14))
<class 'float'>
print(type(True))
<class 'bool'>


# Convert:
print(int("1234")) # Double quoted but using int, it is converted to integer. 
1234
print(int("111") + int("222"))
333
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
Enter your name: Prasanna
Number of letters in your name: 8
Reason: str + str is allowed, str + int is not allowed
Breakdown of the above code:
leng_of_name = input("Enter your name: ")
value_of_leng = len(leng_of_name)
print("Number of letters in your name: " + str(value_of_leng))
Enter your name: Prasanna
Number of letters in your name: 8


# Math opetations:
print("My age: " + str(12))
My age: 12
print(10 + 10)
20
print(10 - 5)
5
print(5 * 5)
25
print(10 ** 5)
100000
print(9 / 2)
4.5
print(9 // 2)
4
print(3 * 3 + 3 / 3 - 3) ### 3*3=9,  3/3=1.0, 9+1.0=10.0, 10.0-3=7.0
7.0
print(3 * (3 + 3) / 3 - 3) ### 3+3=6, 3*6=18, 18/3=6.0, 6.0-3=3.0
3.0


# BMI calculator:
height = 1.65 
weight = 84
height_1 = (height ** 2)
bmi = (weight / height_1)
print(bmi)
30.85399449035813
bmi = (84 / 1.65 ** 2)
print(int(bmi)) ## Ignores the decimal
30 
bmi = (84 / 1.65 ** 2)
print(round(bmi)) ## Make the closest round value
31
bmi = (84 / 1.65 ** 2)
print(round(bmi, 2)) ## Give value with 2 decimals
30.85


# Assignment operators:
score = 0
score += 10
print(score)
10
score = 10
score -= 5
print(score)
5
score = 5
score *= 5
print(score)
25
score = 25
score /= 5
print(score)
5.0
score = 10


# f-strings:
height = 182.5
is_winning = True
print("The overall status is - score: " + str(score) + " height: " + str(height) + " Winning? " + str(is_winning))
The overall status is - score: 10 height: 182.5 Winning? True
height = 182.5
is_winning = True
print(f"The overall status is - score: {score}, height: {height}, is_winning: {is_winning}") 
The overall status is - score: 10, height: 182.5, is_winning: True


# Bill split:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_per = ((bill * tip) / 100)
calcu = ((bill + tip_per) / people)
final_val = round(calcu, 2)
print(f"Each pays {final_val} $")
Welcome to the tip calculator!
What was the total bill? $1555
What percentage tip would you like to give? 10 12 15 55
How many people to split the bill? 5
Each pays 482.05 $
