lines = []
while True:
    lines.append(input("Enter a line of code: "))
    if input("Do you want to end? (y/n): ") == 'y':
        break
for line in lines:
    line = line.replace('>=', 'greater than or equal to')
    line = line.replace('>', 'greater than')
    line = line.replace('<', 'less than')
    line = line.replace('<=', 'less than or equal to')
    line = line.replace('==', 'is equal to')
    line = line.replace(' = ', " is initialized as ")
    line = line.replace('input', "Ask for: ")
    line = line.replace(' int', " Make integer")
    line = line.replace('!=', "is not equal to")
    print(line)