import random
floors = int(input("Enter how many floors the building has: "))
visited = []
while len(visited) < floors:
    randomnum = 0
    while True:
        randomnum = random.randint(1, floors)
        if randomnum not in visited:
            break
    print("Visited Floor: ", randomnum)
    visited.append(randomnum)