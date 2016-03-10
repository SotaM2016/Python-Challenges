layers = int(input("Enter the amount of layers: "))
numbers = []
while layers > 0:
    numbers.append(int(input("Enter the amount for this layer: ")))
    layers -= 1

for number in numbers:
    length = ""
    while number > 0:
        length += "*"
        number -= 1
    print(length)