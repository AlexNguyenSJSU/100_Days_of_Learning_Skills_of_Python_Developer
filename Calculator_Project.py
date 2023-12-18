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

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
user_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

function_operation = operations[user_symbol]
answer = function_operation(num1, num2)

print(f"{num1} {user_symbol} {num2} = {answer}")