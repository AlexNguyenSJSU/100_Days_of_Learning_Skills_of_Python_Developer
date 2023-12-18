import random
word_list = ["aardvark", "baboon", "camel"]

random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in chosen_word:
    display.append('_') 

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

while '_' in display:
    guess = input("Guess a word: ")
    guess = guess.lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            print(display)

print('You win!')