from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

player_1=screen.textinput("PLAYER DETAILS","PLAYER 1 NAME")
player_2=screen.textinput("PLAYER DETAILS","PLAYER 2 NAME")

final_winner = Turtle()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard(player_1,player_2)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
def winner_print(winner):
    final_winner.penup()
    final_winner.color("white")
    final_winner.write("The Winner is "+winner,align="center",font=("Courier",30,"normal"))


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor()<-330:
        ball.bounce_x()


    if ball.xcor()>380:
        ball.reset()
        scoreboard.update_l_score()
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.update_r_score()
    if(scoreboard.l_score==4):
        winner_print(player_1)
        game_is_on=False
    if(scoreboard.r_score==4):
        winner_print(player_2)
        game_is_on=False
screen.exitonclick()
