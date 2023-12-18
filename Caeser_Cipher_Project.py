# Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = [' ', '&', '*', '$', ',', '?', '!', '"', '\\', '~', '_', '^', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ':', ';', '(', ')']

continue_program = True

def caesar(user_text, user_shift, user_direction):
    if user_direction == 'encode':
        cipher_text = ""

        for i in user_text:
            if i in special_characters:
                cipher_text += i
            else:
                index_i = ord(i) - ord('a')
                if index_i + user_shift <= (ord('z') - ord('a')):
                    cipher_text += alphabet[index_i + user_shift]
                else:
                    cipher_text += alphabet[index_i + user_shift - (ord('z') - ord('a')) - 1]
                
        print("The encoded text is " + cipher_text)
    elif user_direction == 'decode':
        plain_text = ""

        for i in user_text:
            if i in special_characters:
                plain_text += i
            else:
                index_i = ord(i) - ord('a')
                if index_i - user_shift >= (ord('a') - ord('a')):
                    plain_text += alphabet[index_i - user_shift]
                else:
                    plain_text += alphabet[index_i - user_shift + (ord('z') - ord('a')) + 1]
                
        print("The decoded text is " + plain_text)

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction != 'encode' and direction != 'decode':
        print('Please type \"encode\" for encrypt the message or \"decode\" for decrypt the message!' )
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # To make sure that the shifting always fits with alphabet:
        shift = shift % 26

        caesar(user_text = text, user_shift = shift, user_direction = direction)

    continue_program_or_not = input('Type \'yes\' if you want to go again. Otherwise type \'no\':\n')
    if continue_program_or_not == 'yes':
        continue_program = True
    elif continue_program_or_not == 'no':
        continue_program = False
    else:
        print('I decided to quit!')
        break