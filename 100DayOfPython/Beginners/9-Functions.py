# Function:
def greet():
    print("Hello World")
    print("How are you?")
    print("What is your name?")
greet()
Hello World
How are you?
What is your name?



# Function with Input:
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
greet_with_name("Prasanna")
Hello Prasanna
How are you Prasanna?



# Question - How many weeks left?
def life_in_weeks(age): # age is parameter
    age_left = 90-age
    age = age_left*52
    print(f"You have {age} weeks left.")
life_in_weeks(35) # 35 is argument 
You have 2860 weeks left.


  
# Function with multiple Inputs:
def greet(name, location):
    print(f"My name is {name} and I am from {location}")
greet("Prasanna", "Madurai")
My name is Prasanna and I am from Madurai



# Function with multiple Inputs with parameters and arguments: 
def greet(name, location):
    print(f"My name is {name}\nI am from {location}")
greet(location="Madurai", name="Prasanna")
My name is Prasanna
I am from Madurai
