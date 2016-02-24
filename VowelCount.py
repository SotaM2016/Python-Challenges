word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
amount = 0
for letter in word:
  if letter in vowels:
    amount += 1
print("There are " + str(amount) + " vowels in that word")
