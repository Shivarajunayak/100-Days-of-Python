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

user_option = int(input("Type 0 for Rock, 1 for Paper, or 2 for scissors: "))
game_images = [rock, paper, scissors]

if user_option > 2:
  print("You entered the wrong number! You lose.")
else:
  print(game_images[user_option])
  computer_option = random.randint(0,2)
  print("Computer Choose:\n", game_images[computer_option])
  
  if user_option == 0 and computer_option == 2 or user_option==2 and computer_option== 1 or user_option == 1 and computer_option == 0:
    print("You win!")
  elif user_option == computer_option:
    print("It's a draw!")
  else:
    print("You lose")     









