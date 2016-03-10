name = input("Enter the name: ")
vowelcount = 0
doubles = False
containsdisabled = False
disabled = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
prevletter = ""
for letter in name:
    if prevletter == letter:
        doubles = True
    elif (prevletter + letter) in disabled:
        containsdisabled = True
    prevletter = letter
    if letter in vowels:
        vowelcount += 1
if doubles == True and containsdisabled == False and vowelcount >= 3:
    print("That person is nice!")
else:
    print("That person is naughty!")