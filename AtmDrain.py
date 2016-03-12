initial = int(input("Enter initial amount of money: "))
withdraw = int(input("Enter the amount you want to withdraw: "))
if withdraw % 5 == 0:
    withdraw += 0.5
    if initial >= withdraw:
        print("Successfully withdrawn money!")
        print("New Balance: " + str(initial - withdraw))
    else:
        print("Insufficient funds to withdraw money!")
else:
    print("The withdraw amount is not a multiple of 5!")