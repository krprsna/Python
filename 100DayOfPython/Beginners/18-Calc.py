# Method 1 - Long way and multipl
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
}

continue_operation = False
while not continue_operation:
    num1 = int(input("Enter the first number: "))
    for i in operations:
        print(i)
    math = input("Enter the operation: ")
    num2 = int(input("Enter the second number: "))
    if math == "+":
        val = add(num1, num2) # Invoking the add function with the input number from user
        print(val)
    elif math == "-":
        val = subtract(num1, num2) # Invoking the subtract function with the input number from user
        print(val)
    elif math == "*":
        val = multiply(num1, num2) # Invoking the multiply function with the input number from user
        print(val)
    elif math == "/":
        val = divide(num1, num2) # Invoking the divide function with the input number from user
        print(val)
    else:
        print("Something went wrong. Try again")
    y_n = input("Would you like to continue? (y/n): ").lower()
    if y_n == "y":
        continue # release the same operation over and again for new calculation.
    elif y_n == "n":
        continue_operation = True



# Method 2 - Short way and multiple use in single execution
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: ")) # THE BEGINING

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ") # Getting the operation symbol 
        num2 = float(input("What is the next number?: ")) 
        answer = operations[operation_symbol](num1, num2) # with the symbol we got from user, we are iterating it with the operations dictinory. Ex: * refers multiply. multiply(n1, n2) function.
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") # recalculate with the previous answer

        if choice == "y":
            num1 = answer # num1 is the previous answer and it confinues from the BEGINING
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # to perform new calc operation
calculator()
