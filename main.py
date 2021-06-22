from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SLEEP = 0.2
# setting up screen
sc = Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)  # setting up screen and off the animation when setup at 0
sc.listen()


t = Turtle()  # for border purpose
t.goto(-290, 290)
t.color("white")
for _ in range(0, 4):
    t.forward(580)
    t.right(90)
t.hideturtle()
t.penup()

# intiliazation of Snake class
snake = Snake()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

# intiliazation of Food class
food = Food()

# intiliazation of Scoreboard class
scoreboard = Scoreboard()

# start the game
game_is_on = True

while game_is_on:
    sc.update()  # update the screen
    snake.move()
    time.sleep(0.1)  # make sure next loop starts in 0.2 sec.

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.incease_length()

    # Detect Collision with Wall
    if snake.head.ycor() > 280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280:
        t.goto(0, 0)
        snake.reset()
        scoreboard.reset()


    # detect Collision with Self
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            t.goto(0, 0)
            snake.reset()
            scoreboard.reset()
            # t.write("GAME OVER", False, "center", font=("Arial", 15, "normal"))
            # game_is_on = False

sc.exitonclick()