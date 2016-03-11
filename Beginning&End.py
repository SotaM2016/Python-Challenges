def getFirst(list):
    return list[0]

def getLast(list):
    return list[len(list) - 1]

lamt = int(input("Enter the amount of numbers you want to put into the list: "))
list = []
current = 1
while current <= lamt:
    list.append(int(input("Enter number (" + str(current) + "): ")))
    current += 1
print("First:", getFirst(list), "Last:", getLast(list))