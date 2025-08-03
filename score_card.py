# Module implemented
import turtle

# Class implemented for creation of scorecard
class Score_Card(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle() # Hiding the unneeded turtle object(arrow-shaped annoyance)
        self.score=0 # Initializing score
        with open("data.txt","r") as file: # Reading and storing the highest game score from a text file
            self.highscore=int(file.read())

    # Function for Increasing and displaying score each swallow from snake
    def increase_score(self):
        self.score+=1
        self.display_score()

   # Function for resetting the game + Storing new high score, if needed
    def  reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt","w") as file:
                file.write(str(self.highscore))
        self.score=0

    # Function for displaying score + scorecard aesthetics
    def display_score(self):
        turtle.clear()
        turtle.goto(0, 270)
        turtle.color("white")
        turtle.write(f"Score= {self.score} Highest Score= {self.highscore}",align="center",font=("Aerial",18,"normal"))



