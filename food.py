# Modules implemented
import turtle
import random

# Class implemented for creation of food
class Food(turtle.Turtle): # Adopting modules from the turtle class
    def __init__(self):
        super().__init__()
        # Setting initializations for features of food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(11)
        self.new_position()

    #  Function for assigning new coordinates for spawning of the "food" object
    def new_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
