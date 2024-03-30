import random

rock = '''
      _ _ _ _ 
_ _ _'  _ _ _)
       (_ _ _ _)
       (_ _ _ _)
_ _ _  (_ _ _)
     '_(_ _)
'''

paper = '''
      _ _ _ _ _ 
_ _ _'   _ _ _ _)_ _ _ _
              _ _ _ _ _ _)
              _ _ _ _ _ _ _)
_ _ _         _ _ _ _ _ _ )
     '_ _ _ _ _ _ _ _ )
'''


scissors = '''
      _ _ _ _ _ _ 
_ _ _'      _ _ _)_ _ _ _
            _ _ _ _ _ _ _)
            _ _ _ _ _ _ _ _ )
_ _ _       _ _ _ _ _)
     '_ _ _ _ _ _ _)
'''

game_images = [rock,paper,scissors]
user_choice = int(input("enter your choice: Type 1 for rock, 2 for paper, 3 for scissors:"))
if user_choice >= 3 or user_choice <0:
    print("you have entered worng input , You lost.")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice ])
    if computer_choice == user_choice:
        print("it's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice :
        print(" You win.")