from turtle import Turtle

SCORE = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt", mode="r") as file:
            self.highscrore = int(file.read())
        self.score = SCORE
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score is {self.score}, Highest Score:{self.highscrore}", False, "center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscrore:
            self.highscrore = self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscrore}")

    def increase_score(self):
        self.score += 1