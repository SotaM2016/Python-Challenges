filename = input("Enter the file name: ")
content = ""
with open(filename, 'r') as content_file:
    content = content_file.read()
strings = content.split(' ')
total = 0
amount = 0
for string in strings:
    total += len(string)
    amount += 1
print("The average word length in the file is: " + str(total/amount))