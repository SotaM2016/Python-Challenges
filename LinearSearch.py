lamt = int(input("Enter the amount of numbers you want to put into the list: "))
list = []
current = 1
while current <= lamt:
    list.append(int(input("Enter number (" + str(current) + "): ")))
    current += 1
search = int(input("Enter what you want to find: "))
found = False
current = 0
for num in list:
    if num == search:
        print("Your search has been found as number", current + 1, " in the list")
        found = True
    current += 1
if not found:
    print("Your number was not in the list!")