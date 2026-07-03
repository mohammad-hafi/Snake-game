from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highest_score=int(data.read())

        self.new=0
        self.color("orange")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score} high score:{self.highest_score}",move=False,align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def reset(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score=0
        self.clear()
        self.write(f"Score: {self.score}  high score:{self.highest_score}",move=False,align="center",font=("Arial",24,"normal"))



    def newscore_inc(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score} high score:{self.highest_score}",move=False,align="center",font=("Arial",24,"normal"))













