# Sample program for dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary)
{'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.'}

print(programming_dictionary["Bug"]) # Print only the given key:value
An error in a program that prevents the program from running as expected.

programming_dictionary["Loop"] = "Action that is repeated over and over again" # Append new key:value
print(programming_dictionary)
{'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'Action that is repeated over and over again'}

programming_dictionary["Loop"] = "Action that is executed again and again" # Edit the existing key:value
print(programming_dictionary)
{'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'Action that is executed again and again'}


# Using for loop with dic
for i in programming_dictionary:
    print(i) # Prints only the key
Bug
Function
Loop


# Using for loop with dic
for i in programming_dictionary:
    print(programming_dictionary[i]) # Prints both the key:value
Bug
An error in a program that prevents the program from running as expected.
Function
A piece of code that you can easily call over and over again.
Loop
Action that is executed again and again

