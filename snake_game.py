# Classic Snake Game Project

#-----------------------------
# Modules imported and implemented
import turtle as t
import time
from snake import snake
import food
import score_card

t.hideturtle() # Used to hide the arrow at the start.

# Screen setup and aesthetics
screen=t.Screen()
screen.bgcolor("black")
screen.title("The Sneaky Slytherin Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0) # Turing off automatic screen updates
screen.listen() # Used to listen to keyboard clicks from user

segments=[] # This is absolutely, utterly, completely....useless. Kept as a mark of my dunderness

game_on=True

# Creating the snake object + Sending current screen to class "snake"
snake=snake(screen)

# Creating the food object using class "Food"
food=food.Food()

# Creating the scorecard object using class "Score_Card"
score=score_card.Score_Card()


while game_on:
    screen.update() # Manually making the screen re-draw everything after one full loop
    time.sleep(0.1) # Slowing loop down, else the snake will act like a Slytherin forced to be a Hufflepuff....absolute chaos!
    snake.move()
    score.display_score()

    #Detecting collision of snake with food
    if snake.segments[0].distance(food) < 17:
        food.new_position()
        snake.add_segment_at_tail()
        score.increase_score()

    #Detecting collision with boundaries + Resetting the game + Storing the score if it's highest  yet
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        score.reset()
        snake.reset()


    #Detecting collision with snake body + Resetting the game + Storing the score if it's highest yet
    segments_without_head=snake.segments[1:] # String-slicing to access snake body
    for segment in segments_without_head:
        if segment.distance(snake.segments[0])<8:
            score.reset()
            snake.reset()



screen.exitonclick()