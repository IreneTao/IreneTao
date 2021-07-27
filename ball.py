from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.shape("circle")
        self.penup()
        self.movex = 10
        self.movey = 10
        self.move_speed = 0.1


    def move(self):
        new_x= self.xcor() + self.movex
        new_y= self.ycor() + self.movey
        self.goto(new_x, new_y)
        self.speed("fast")

    def bounce_y(self):
        self.movey *= -1

    def bounce_x(self):
        self.movex *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()













