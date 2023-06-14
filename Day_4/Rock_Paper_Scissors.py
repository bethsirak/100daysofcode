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
rps = [rock, paper, scissors]

#Player 
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
choice_int = int(choice)

if choice_int >=3 or choice_int<0:
  print("You typed an invalid number, you lose!")
else:
  print(rps[choice_int])

  #Computer: Get a random number between 0-2
  random_integer = random.randint(0,2)
  choice_computer = rps[random_integer]
  
  print(f"Computer chose: {choice_computer}")
  
  if choice_int == random_integer:
    print("You tie")
  elif choice_int == 0 and random_integer == 2:
      print("You win!")
  elif random_integer == 0 and choice_int == 2:
      print("You lose!")
  elif choice_int > random_integer:
    print("You win!")
  elif choice_int < random_integer:
    print("You lose!")