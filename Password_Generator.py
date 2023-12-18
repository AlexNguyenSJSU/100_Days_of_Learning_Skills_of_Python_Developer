import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result = ''

for i in range(nr_letters):
    index_letter = random.randint(0, len(letters) - 1)
    result += letters[index_letter]

for i in range(nr_symbols):
    index_symbol = random.randint(0, len(symbols) - 1)
    result += symbols[index_symbol]

for i in range(nr_numbers):
    index_num = random.randint(0, len(numbers) - 1)
    result += numbers[index_num]

list_result = random.sample(result, len(result))
password = "".join(list_result)

print("Here's your password: " + password)