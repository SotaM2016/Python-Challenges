import random
import tkinter

def getRandNo():
    return int(''.join([random.choice('0123456789') for x in range(2)]))

def hexQuiz(window, randno):
    window.wm_title("Hexadecimal Quiz")
    quizl = tkinter.Label(window, text="Translate this into Hexadecimal: " + str(randno))
    quizl.pack()
    ansbox.bind("<Return>", hexAnswer)
    ansbox.pack()
    return

def binQuiz(window, randno):
    window.wm_title("Binary Quiz")
    quizl = tkinter.Label(window, text="Translate this into Binary: " + str(randno))
    quizl.pack()
    ansbox.bind("<Return>", binAnswer)
    ansbox.pack()
    return

def binAnswer(event):
    answer = ansbox.get()
    if answer == str(bin(randno)):
        errorbox.configure(text="Correct!")
    else:
        errorbox.configure(text="Wrong! Answer: " + str(bin(randno)))
    ansbox.configure(text=" ")
    return

def hexAnswer(event):
    answer = ansbox.get()
    if answer == str(hex(randno)):
        errorbox.configure(text="Correct!")
    else:
        errorbox.configure(text="Wrong! Answer: " + str(hex(randno)))
    ansbox.configure(text=" ")
    return

window = tkinter.Tk()
type = input("Enter whether you want a hex quiz or bin quiz: ")
ansbox = tkinter.Entry(window)
randno = getRandNo()
errorbox = tkinter.Label(window)
if type == 'Hex':
    hexQuiz(window, randno)
else:
    binQuiz(window, randno)
errorbox.pack()
window.mainloop()