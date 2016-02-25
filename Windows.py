import tkinter
from random import randint
filename = input("Enter the file name: ")
content = ""
with open(filename, 'r') as content_file:
    content = content_file.read()
strings = content.split(' ')
window = tkinter.Tk()
title = tkinter.Label(window, text = "Random Name Picker", font="Helvetica 16 bold")
title.pack()
label = tkinter.Label(window, text = "Your random name: " + strings[randint(0, len(strings)) - 1], font="Helvetica 16 bold")
label.pack()
window.mainloop()