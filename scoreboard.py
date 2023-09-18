from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
            file.close()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
                file.close()
        self.score = 0
        self.update()