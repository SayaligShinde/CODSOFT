import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺'))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
   
    print('Player choice is ', choice_name)
    

    computer_choice = random.randint(1, 3)

    while computer_choice == choice:
        computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice_name = 'RocK'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'
    print("Computer choice is ", computer_choice_name)
    print(choice_name, 'Vs', computer_choice_name)
   
    if choice == computer_choice:
        print('Its a Tie', end="")
        result = "Tie"
  
    if (choice == 1 and computer_choice == 2):
        print('paper wins ', end="")
        result = 'Paper'
    elif (choice == 2 and computer_choice == 1):
        print('paper wins ', end="")
        result = 'Paper'

    if (choice == 1 and computer_choice == 3):
        print('Rock wins ', end="")
        result = 'Rock'
    elif (choice == 3 and computer_choice == 1):
        print('Rock wins ', end="")
        result = 'RocK'

    if (choice == 2 and computer_choice == 3):
        print('Scissors wins ', end="")
        result = 'Scissors'
    elif (choice == 3 and computer_choice == 2):
        print('Scissors wins ', end="")
        result = 'Rock'

    if result == 'DRAW':
        print(" Its a Tie ")
    if result == choice_name:
        print(" \nUser Wins!!! ")
    else:
        print(" \nComputer Wins!!! ")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break
    
print("Thanks for Playing!!!")