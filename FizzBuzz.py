import tkinter
import time

def number(number):
    label.configure(text = str(number))
    return

def fizz():
    label.configure(text = "Fizz")
    return

def buzz():
    label.configure(text = "Buzz")
    return

def fizzbuzz():
    label.configure(text = "FizzBuzz")
    return

def counter(currentn):
    print(currentn)
    if currentn % 5 == 0:
        if currentn % 3 == 0:
           fizzbuzz()
        else:
            buzz()
    elif currentn % 3 == 0:
        fizz()
    else:
        number(currentn)
    currentn += 1
    window.update_idletasks()
    window.update()
    if currentn <= 20:
        time.sleep(1)
        counter(currentn)
    else:
        time.sleep(2)
    return

window = tkinter.Tk()
title = tkinter.Label(window, text = "Fizz Buzz Game", font="Helvetica 16 bold")
title.pack()
label = tkinter.Label(window, text = "Fizz Buzz", font="Helvetica 16 bold")
label.pack()
counter(0)