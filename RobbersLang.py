hidden = input("Input the string you want encoded: ")
new = ""
for alph in hidden:
    new += alph + "o" + alph
print(new)