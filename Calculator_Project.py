# CALCULATOR PROJECT:
from art import logo

# Adding
def add (n1, n2):
    return (n1 + n2)

# Subtracting
def subtract (n1, n2):
    return (n1 - n2)

# Multiplying
def multiply (n1, n2):
    return (n1 * n2)

# Dividing
def divide (n1, n2):
    return (n1 / n2)

# Powering
def power (n1, n2):
    return (n1 ** n2)

# Dict for storing the operation functions:
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': power
}

def calculator():
    print(logo)
    check_loop = 'y'

    num1 = float(input("What's the first number?: "))

    while check_loop == 'y':
        for symbol in operations:
            print(symbol)
        user_symbol = input("Pick an operation from the line above: ")

        num_next = float(input("What's the next number?: "))

        function_operation = operations[user_symbol]
        answer = function_operation(num1, num_next)

        print(f"{num1} {user_symbol} {num_next} = {answer}")

        check = input(f"Type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculation: ")
        if check == 'y':
            num1 = answer
        else:
            check_loop = 'n'
            calculator()

calculator()