import tkinter

def addOne():
    global one
    one += 1
    return

def addTwo():
    global two
    two += 1
    return

def addThree():
    global three
    three += 1
    return

def addFour():
    global four
    four += 1
    return

one = 0
two = 0
three = 0
four = 0

window = tkinter.Tk()
onel = tkinter.Button(window, text="1", command=addOne)
onel.pack()
twol = tkinter.Button(window, text="2", command=addTwo)
twol.pack()
threel = tkinter.Button(window, text="3", command=addThree)
threel.pack()
fourl = tkinter.Button(window, text="4", command=addFour)
fourl.pack()
window.mainloop()
print("Clicked Amount: ")
print("One:", one, "Two:", two, "Three:", three, "Four:", four)