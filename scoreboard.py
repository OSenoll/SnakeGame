from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()


    def update(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        print("Game Over")
