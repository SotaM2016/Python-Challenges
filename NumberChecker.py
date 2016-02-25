def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

test = input("Enter a float: ")
if isNumber(test):
    print("That is a float!")
else:
    print("That is not a float!")