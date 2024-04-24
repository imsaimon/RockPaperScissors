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

# Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors Game!")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
    print(paper)
if choice == 1:
    print(scissors)
if choice == 2:
    print(rock)

print("Computer chose:")
import random

random_choice = random.randint(0, 2)
if random_choice == 0:
    print(paper)
if random_choice == 1:
    print(scissors)
if random_choice == 2:
    print(rock)

if choice == 0 and random_choice == 0:
    print("Draw")
if choice == 0 and random_choice == 1:
    print("You lose")
if choice == 0 and random_choice == 2:
    print("You win")
if choice == 1 and random_choice == 0:
    print("You win")
if choice == 1 and random_choice == 1:
    print("Draw")
if choice == 1 and random_choice == 2:
    print("You lose")
if choice == 2 and random_choice == 0:
    print("You lose")
if choice == 2 and random_choice == 1:
    print("You win")
if choice == 2 and random_choice == 2:
    print("Draw")