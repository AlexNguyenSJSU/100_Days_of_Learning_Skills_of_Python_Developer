rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = [rock, paper, scissors]
print(len(choice))

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if your_choice >= len(choice) or your_choice < 0:
    print("You typed invalid choice! LOSER!")
else:
    computer_choice = random.randint(0, 2)

    print(choice[your_choice])
    print("Computer choose: \n" + choice[computer_choice])
    
    if your_choice == computer_choice:
        print("Draw!")
    elif your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif  your_choice == 1 and computer_choice == 0:
        print("You win!")
    elif your_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose. LOSER!")