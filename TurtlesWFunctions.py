import turtle
__import__("turtle").__traceable__ = False

def drawColoredSq(t, size):
    for color in ['red', 'blue', 'yellow', 'green']:
        t.color(color)
        t.forward(size)
        t.left(90)

window = turtle.Screen()
pensize = int(input("Enter pen size: "))
bgcolor = input("Enter background color: ")
loop = int(input("Enter how many times to loop: "))
size = int(input("Enter initial size: "))
offset = int(input("Enter offset per square: "))
tess = turtle.Turtle()
tess.pensize(pensize)
window.bgcolor(bgcolor)

for i in range(loop):
    drawColoredSq(tess, size)
    size += offset
    tess.forward(10)
    tess.left(18)
window.mainloop()