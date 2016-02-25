from random import randint
# 0 = Scissors, 1 = Papers, 2 = Stone
player = input("Choose Scissors, Paper, or Stone: ")
pc = randint(0, 2)
if pc == 0:
    if player == "Scissors":
        print("Tie!")
    elif player == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif pc == 1:
    if player == "Scissors":
        print("You win!")
    elif player == "Paper":
        print("Tie!")
    else:
        print("You lose!")
elif pc == 2:
    if player == "Scissors":
        print("You lose!")
    elif player == "Paper":
        print("You win!")
    else:
        print("Tie!")