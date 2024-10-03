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
import random
game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You chose a invalid number. Perhaps read the instructions again!")
else:
    print(game[choice])
    print("Computer chose:\n")
    comp_choice = random.randint(0, 2)
    print(game[comp_choice])
    if comp_choice == choice:
        print("You Draw")
        print("Go again")
    elif comp_choice == 0 and choice == 1:
        print("You Win!")
    elif comp_choice == 1 and choice == 2:
        print("You Win!")
    elif comp_choice == 2 and choice == 0:
        print("You Win!")
    else:
        print("You Lose")
        print("Try again?")
