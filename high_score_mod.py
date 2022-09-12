import turtle as t

class HighScore(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('purple')
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def score_increase(self):
        self.clear()
        self.high_score += 1
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def show_score(self, updated_value):
        self.clear()
        self.high_score = updated_value
        self.write(f"HIGH SCORE: {self.high_score}", align="center", font=("Courier", 12, "normal"))