from turtle import Screen
from snake import Snake
import time
from scoreboard import Score
from food import Food
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("welcome to my snake game")
snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)



gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.newscore_inc()

        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for seg in snake.mytur:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()





screen.exitonclick()

