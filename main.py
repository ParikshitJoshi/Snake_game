from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("SNAKE GAME")
Screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
food.refresh()

Screen.listen()
Screen.onkey(snake.up, "w")
Screen.onkey(snake.down, "s")
Screen.onkey(snake.left, "a")
Screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.1)

    snake.move()

    # colliding with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # colliding with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # colliding with tail
    for segment in snake.segment[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






Screen.exitonclick()
