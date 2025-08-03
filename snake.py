# Modules implemented
import turtle as t
import time

# Class implemented for creation of the snake
class snake:
    def __init__(self,screen):
        self.screen=screen
        self.segments = [] # Will be used to store snake's body...Creepy, I know.
        self.create_snake()

    # Function for creating snake + Snake aesthetics
    def create_snake(self,x=0,y=0):
        # The for loop combines three turtle objects to make a snake body
        for i in range(0, 3):
            snake_part = t.Turtle() # Using turtle to create snake object
            snake_part.penup()
            snake_part.shape("square")
            snake_part.color("white")
            snake_part.goto(x, y)
            self.segments.append(snake_part) # Storing snake's growing body in a list for easy iteration later on
            x -= 20 # This ensures that new body part spawns 20 units to left of the previous one

    # Function for extending snake's body at the tail
    def add_segment_at_tail(self):
        snake_part = t.Turtle() # Using turtle to create new body parts to elongate snake
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.goto(self.segments[-1].xcor(), self.segments[-1].ycor()) # Adding at the tail of the snake using end coordinates
        self.segments.append(snake_part)

    # Snake moves in different directions(right/left/up/down), but never the opposite of current direction
    def turn_right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    # Function for resetting game + Creating new snake body
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,10000)
        self.segments.clear()
        self.create_snake()

    # Function for allowing snake movement + Listening to user's keyboard-clicks
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(20)

        # Snake's movement directions are recorded and acted upon
        self.screen.onkey(key="Right",fun=self.turn_right)
        self.screen.onkey(key="Left",fun=self.turn_left)
        self.screen.onkey(key="Up",fun=self.turn_up)
        self.screen.onkey(key="Down",fun=self.turn_down)



