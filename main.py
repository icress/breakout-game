from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Score
import time

speed = 0.02
colors = ['purple', 'red', 'orange', 'yellow', 'green']

screen = Screen()

screen.setup(height=800, width=900)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle = Paddle()
paddle.setposition(x=0, y=-300)

screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

ball = Ball()

score = Score()

x_pos = -470
y_pos = 400
color_num = 0
brick_list = []

for num in range(50):
    brick = Brick()
    if num % 10 == 0 and num != 0:
        color_num += 1
    brick.color('white', colors[color_num])
    if num % 10 == 0:
        y_pos -= 55
        x_pos = -470
    x_pos += 85
    brick.setposition(y=y_pos, x=x_pos)
    brick_list.append(brick)

game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move_ball()

    if ball.distance(paddle) < 120 and ball.ycor() < -270:
        ball.bounce_y()

    if ball.ycor() > 410:
        ball.bounce_y()

    if ball.xcor() > 420 or ball.xcor() < -420:
        ball.bounce_x()

    for brick in brick_list:
        if brick.distance(ball) < 50:
            if abs(ball.xcor() - brick.xcor()) > 35:
                ball.bounce_x()
            else:
                ball.bounce_y()
            brick_list.remove(brick)
            brick.reset()
            if not brick_list:
                game_on = False
                score.win()

    if ball.ycor() < -380:
        game_on = False
        score.game_over()

screen.exitonclick()
