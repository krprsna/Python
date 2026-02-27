# Convert the 1st letter into UPPER case for the given input.
# Method 1
def format_name(f_name, l_name):
    return (f_name +" "+ l_name).title() # End of the program within the function
print(format_name("prasanna", "kr"))
Prasanna Kr

# Method 2
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name("AnGEla", "YU"))
Angela Yu



# Indivudual function does two different operation 
def func_1(text):
    return text + text # End of the program within the function
print(func_1("prasanna"))
prasannaprasanna

def func_2(text):
    return text.title() # End of the program within the function
print(func_2("prasanna"))
Prasanna



# Output of a function is used as input for the another fumction
def func_1(text):
    return text + text # End of the program within the function
def func_2(text):
    return text.title() # End of the program within the function
print(func_1(func_2("prasanna"))) 
PrasannaPrasanna

print(func_2(func_1("prasanna")))
Prasannaprasanna



# Getting user input in function:
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("Enter First name :"), input("Enter Last name :")))
Enter First name :prasanna
Enter Last name :kr
Prasanna Kr



# Using if statement to show the usage of return
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You have entered invalid name" # If this satisfies the program ends here
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("Enter First name :"), input("Enter Last name :")))
Enter First name :
Enter Last name :
You have entered invalid name

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You have entered invalid name" # if valid data is given, the program will run rest of the command
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
print(format_name(input("Enter First name :"), input("Enter Last name :")))
Enter First name :prasanna
Enter Last name :kr
Result: Prasanna Kr
