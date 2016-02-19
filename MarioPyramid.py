amt = int(input("Enter the size of the pyramid: "))
loop = 1
while loop <= amt:
    pyramid = loop
    current = ""
    while pyramid > 0:
        current += "x"
        pyramid -= 1
    print(current)
    loop += 1