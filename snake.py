from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # initialind the class with constructor by storing the values of each turtle created in the game
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.speed("fastest")
            self.segment.append(new_segment)

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[i - 1].xcor()
            y_cor = self.segment[i - 1].ycor()
            self.segment[i].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def incease_length(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        x_cor = self.segment[len(self.segment) - 1].xcor()
        y_cor = self.segment[len(self.segment) - 1].ycor()
        new_segment.goto(x_cor, y_cor)
        self.segment.append(new_segment)
