############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.
from art import logo
import random

check_repeat = True

while check_repeat:
    # Logo Printing:
    print(logo)

    # Deal cards for users:
    user_cards = []
    for i in range(0, 2):
        user_card = random.choice(cards)
        user_cards.append(user_card)

    print(f'Your cards: {user_cards}')
    
    # Deal cards for dealer (computer):
    comp_cards = []
    for i in range(0, 2):
        comp_card = random.choice(cards)
        comp_cards.append(comp_card)

    # Calculate the sum for both users and computer:
    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)

    # Checking the blackjack for both users and computer:
    if comp_sum == 21:
        print('Blackjack for Dealer! You LOSE! What a Failure!')

        # Repeating the game or not:
        input_user = 'y'
        while input_user == 'y' or input_user == 'n':
            input_user = input("Do you want to play Blackjack more? Type \'y\' or \'n\': ")
            if input_user == 'y':
                check_repeat = True
                break
            elif input_user == 'n':
                check_repeat = False
                break
    elif user_sum == 21:
        print('Blackjack! You Win!')
        
        # Repeating the game or not:
        input_user = 'y'
        while input_user == 'y' or input_user == 'n':
            input_user = input("Do you want to play Blackjack more? Type \'y\' or \'n\': ")
            if input_user == 'y':
                check_repeat = True
                break
            elif input_user == 'n':
                check_repeat = False
                break

    # Replace Ace with 11 to 1 if needed (both users and computer):
    if user_sum > 21 and 11 in user_cards:
        user_sum -= 11
        user_sum += 1
    if comp_sum > 21 and 11 in comp_cards:
        comp_sum -= 11
        comp_sum += 1

    # Reveal the first card of the computer/dealer:
    print(f'Computer\'s first card: {comp_cards[0]}')
    # Testing Purpose: print(comp_cards)

    # Checking whether the user wins or loses:
    if user_sum > 21:
        print('Blackjack for Dealer! You LOSE! What a Failure!')
        break

    # Dealing another card for the user if he/she wants to:
    dealt_another_card = 'hit'
    while dealt_another_card == 'hit' or dealt_another_card == 'stand':
        dealt_another_card = input("Type \'hit\' for another card, otherwise Type \'stand\' for stop this process: ")
        if dealt_another_card == 'hit':
            user_card = random.choice(cards)
            user_cards.append(user_card)
            # Testing purpose: 
            print(user_cards)
            user_sum = sum(user_cards)
            if user_sum > 21 and 11 in user_cards:
                user_sum -= 11
                user_sum += 1
            break
        elif dealt_another_card == 'stand':
            print('OK! Let\'s see...')
            break

    # If the sum of the computer/dealer's card values is not > 16, do this:
    while comp_sum <= 16:
        comp_card = random.choice(cards)
        comp_cards.append(comp_card)
        # Testing purpose: print(comp_cards)
        comp_sum += comp_card
    
    if comp_sum > 21 and 11 in comp_cards:
        comp_sum -= 11
        comp_sum += 1

    # Compare to see who's the winner:
    if user_sum == comp_sum:
        print('PUSH! Lucky for ya! Hehe...')
    elif user_sum > 21:
        print('You LOSE! What a Failure!')
    elif comp_sum > 21:
        print('You Win!')
    elif user_sum > comp_sum:
        print('You Win!')
    else:
        print('You LOSE! What a Failure!')
    
    # The Scores of both sides:
    print(f'The final result of the User: {user_sum}')
    print(f'The final result of the Dealer: {comp_sum}')

    # Repeating the game or not:
    input_user = 'y'
    while input_user == 'y' or input_user == 'n':
        input_user = input("Do you want to play Blackjack more? Type \'y\' or \'n\': ")
        if input_user == 'y':
            check_repeat = True
            break
        elif input_user == 'n':
            check_repeat = False
            break