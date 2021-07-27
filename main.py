from turtle import Turtle, Screen
from bar import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

r_paddle= Paddle((350, 0))
l_paddle= Paddle((-350, 0))

ball= Ball()


score = Scoreboard()


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


    #BALL COLLISION TOP AND BOTTOM WALLS
    current_y= ball.ycor()
    if current_y > 280 or current_y <-280:
        ball.bounce_y()

    #DETECT COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #DETEC WHEN PADDLE MISSES
    if ball.xcor() >380:
        score.l_paddle_score()
        ball.restart()
    elif ball.xcor() < -380:
        score.r_paddle_score()
        ball.restart()
    else:
        pass



screen.exitonclick()