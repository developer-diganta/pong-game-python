from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,playe_1,playe_2):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.player_1=playe_1
        self.player_2=playe_2
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.player_1+":"+str(self.l_score),align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.player_2+":"+str(self.r_score),align="center",font=("Courier",80,"normal"))

    def update_l_score(self):
        self.l_score+=1
        self.update_scoreboard()


    def update_r_score(self):
        self.r_score+=1
        self.update_scoreboard()



