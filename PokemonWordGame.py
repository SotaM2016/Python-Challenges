import random
content = ""
with open("PokemonNames.txt", 'r') as content_file:
    content = content_file.read()
strings = content.split('\n')
used = []
currentp = 1
previous = ""
while True:
    if previous == "":
        previous = random.choice(strings)
        print("Starting word (P1): " + previous)
        strings.remove(previous)
    else:
        next = ""
        for pokemon in strings:
            if pokemon[0] == previous[len(previous) - 1].upper():
                next = pokemon
                break
        if next == "":
            break
        else:
            print("Next word (P" + str(currentp) + "): ", next)
            previous = next
            strings.remove(next)
    currentp += 1
    if currentp > 2:
        currentp = 1
print("Player " + str(currentp) + " loses the game!")