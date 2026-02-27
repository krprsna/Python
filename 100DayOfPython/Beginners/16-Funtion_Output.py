# Convert the 1st letter into UPPER case for the given input.
def format_name(f_name, l_name):
    return (f_name +" "+ l_name).title()
print(format_name("prasanna", "kr"))
Prasanna Kr


# Indivudual function does two different operation 
def func_1(text):
    return text + text
print(func_1("prasanna"))
prasannaprasanna

def func_2(text):
    return text.title()
print(func_2("prasanna"))
Prasanna


# Output of a function is used as input for the another fumction
def func_1(text):
    return text + text
def func_2(text):
    return text.title()
print(func_1(func_2("prasanna"))) 
PrasannaPrasanna

print(func_2(func_1("prasanna")))
Prasannaprasanna
