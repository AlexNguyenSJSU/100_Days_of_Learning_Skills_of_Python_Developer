import os
from art import logo

def clear_console():
    # Clear the console screen (works on various platforms)
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print('Welcome to the secret auction program')

dict_users = {}

next_or_end = 'yes'

while next_or_end == 'yes':
    name = input('What is your name? ')
    bid_value = float(input('what\'s your bid? $'))

    dict_users[name] = bid_value
    question_end_or_next = input('Are there any other bidders? ')
    if question_end_or_next == next_or_end:
        clear_console()
    elif question_end_or_next.lower() == "no":
        break
    else:
        check = False
        while not check:
            question_end_or_next = input('Invalid answer, please type again: yes/no? ')
            if question_end_or_next == next_or_end:
                clear_console()
                check = True
            else:
                next_or_end = 'no'
                check = True


winner_name = max(dict_users, key = dict_users.get)
winning_bid = dict_users[winner_name]

print(f"The winner is {winner_name} with a bid of ${winning_bid:.2f}")