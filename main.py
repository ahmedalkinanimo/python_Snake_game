from turtle import Screen
from Snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(800, 800)
    screen.title("Snake")
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = ScoreBoard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detecting collision with the snake
        if snake.head.distance(food) < 15:
            food.refresh()
            score_board.score_update()
            snake.extend()

        # detect collision with the wall
        if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
            game_on = False
            score_board.game_over()

        # detect collision with the tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score_board.game_over()

    screen.exitonclick()
