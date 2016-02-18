from random import randint

rnum = randint(1,100)
guess = input("Make your guess: ")

guess = int(guess)
if guess > 100:
    print("Your number has to be less than 100")
elif guess < 1:
    print("Your number has to be more than 0")
else:
    if guess == rnum:
        print("Your guess is correct!")
    else:
        print("Your guess is wrong!")
        print("The correct answer is: " + str(rnum))