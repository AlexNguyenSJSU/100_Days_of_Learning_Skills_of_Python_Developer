# Version 1 of my HangMan project:

import random
import Version_1_HangMan_Day_7.support_words as support_arts
import Version_1_HangMan_Day_7.support_words as support_words

end_of_game = False

# Importing from another files to use different variables:
words = support_words.word_list
user_stage = support_arts.stages
game_logo = support_arts.logo

print(game_logo)

# Choosing the word randomly:
random_index = random.randint(0, len(words) - 1)
chosen_word = words[random_index]

word_length = len(chosen_word)

# Keep track of the number of lives left:
lives = 6
count = 0

# Testing code:
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks:
display = []

for i in chosen_word:
    display.append('_') 

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if a letter they've already guessed, print the letter and notification:
    if guess in display:
        print("You've already guessed: " + guess)
        print(f"{' '.join(display)}")
    else:
        # Check guessed letter:
        for position in range(word_length):
            letter = chosen_word[position]
            
            if letter == guess:
                display[position] = letter

        # If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if not guess in display:
            lives -= 1
            count += 1
            print('You guessed ' + guess + f' , that is not in the word. You lose {count} life/lives!')
            if lives == 0: 
                print('You lose!')
                print(user_stage[0])
                print('The correct word is: ' + chosen_word)
                break

        # Join all the elements in the list and turn it into a String:
        print(f"{' '.join(display)}")

        # Check if user has got all letters:
        if "_" not in display:
            end_of_game = True
            print("You win.")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining:
    print(user_stage[lives])