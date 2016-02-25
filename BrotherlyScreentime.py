import time

atime = int(input("Enter the total time allowed (s): "))
sib = int(input("Enter the amount of siblings: "))
while sib > 0:
    time.sleep(atime/sib)
    if sib == 1:
        print("Game time is over!")
    else:
        print("Time is up! Swap to the next sibling!")
    sib -= 1