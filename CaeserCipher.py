type = input("Choose, Encoder or Decoder: ")
string = input("Enter your text: ")
if type=="Encoder":
    ntext = ""
    for letter in string:
        if letter != " ":
            lid = ord(letter)
            if lid == 122:
                lid = 97
            elif lid == 90:
                lid = 65
            else:
                lid += 1
            ntext += chr(lid)
        else:
            ntext += " "
    print(ntext)
elif type=="Decoder":
    ntext = ""
    for letter in string:
        if letter != " ":
            lid = ord(letter)
            if lid == 97:
                lid = 122
            elif lid == 65:
                lid = 90
            else:
                lid -= 1
            ntext += chr(lid)
        else:
            ntext += " "
    print(ntext)
