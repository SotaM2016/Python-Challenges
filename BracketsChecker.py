text = input("Enter a text you want to check: ")
inwards = 0
outwards = 0
for string in text:
  if string == '(':
    inwards += 1
    elif string == ')':
      outwards += 1
if inwards == outwards:
  print("The amount of brackets are the same")
else:
  print("The amount of brackets are not the same")
