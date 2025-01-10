# Pong Game
# TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
# TODO 4: Create  the ball and make it move
# TODO 5: Detect collision with  wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep scorew

from turtle import Screen
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        if scoreboard.l_score == 5:
            turtle.goto(0,-40)
            turtle.color('white')
            turtle.write("Left player won", align='center', font=('Arial', 24, 'normal'))
        elif scoreboard.r_score == 5:
            turtle.goto(0,-40)
            turtle.color('white')
            turtle.write("Right player won", align='center', font=('Arial', 24, 'normal'))
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

