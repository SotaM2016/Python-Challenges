import turtle
from random import randint
turns = int(input("Enter the amount of turns the pirate makes: "))
window = turtle.Screen()
pirate = turtle.Turtle()
while turns > 0:
  random = randint(0, 360)
  pirate.right(random)
  pirate.forward(100)
  turns -= 1
