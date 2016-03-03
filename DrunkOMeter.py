typestring = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
answer = input("Type in the following phrase: " + typestring)

if answer == typestring:
    print("Correct!")
    answer = input("Now type it again: ")
    if answer == typestring:
        print("Well done! You have passed the test")
    else:
        print("You are not worthy enough for this job!")
else:
    print("You are not worthy enough for this job!")