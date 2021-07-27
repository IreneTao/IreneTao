from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()



    def score_update(self):
        self.goto(-100,200)
        self.write(self.l_score, align ="left", font= ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="right", font=("Courier", 80, "normal"))


    def l_paddle_score(self):
        self.l_score += 1
        self.clear()
        self.score_update()



    def r_paddle_score(self):
        self.r_score +=1
        self.clear()
        self.score_update()





