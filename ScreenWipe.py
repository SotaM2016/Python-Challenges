print("Clearing Screen...")
amount = 0
while amount < 20:
    print(chr(27) + "[2J")
    amount += 1
print("Cleared!")