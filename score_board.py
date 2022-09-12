from turtle import Turtle
import  time

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 22, "normal"))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 22, "normal"))

    def game_over(self):
        game_over = Turtle()
        game_over.color("purple")
        game_over.goto(0, 0)
        game_over.write(f"GAME OVER", align="center", font=("Arial", 40, "bold"))
        time.sleep(0.5)
        game_over.clear()
        game_over.hideturtle()
        time.sleep(0.25)
