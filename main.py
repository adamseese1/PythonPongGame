from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
# screen.bgpic("frog.png")
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ##Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect if ball goes past the paddle and hits wall
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    ##Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if the game is over
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()