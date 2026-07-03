from turtle import Turtle
places=[(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self):
        self.mytur=[]
        self.make_snake()
        self.head=self.mytur[0]

    def make_snake(self):
        for pos in places:
            self.add_segment(pos)
    def add_segment(self,pos):
        newturtle = Turtle(shape="square")
        newturtle.penup()
        newturtle.color("white")
        newturtle.goto(pos)
        newturtle.speed("fastest")
        self.mytur.append(newturtle)
    def reset(self):
        for sed in self.mytur:
            sed.goto(1000,1000)
        self.mytur.clear()
        self.make_snake()
        self.head = self.mytur[0]


    def extend(self):
        self.add_segment(self.mytur[-1].position())


    def snake_move(self):
        for sum in range(len(self.mytur) - 1, 0, -1):
            new_x = self.mytur[sum - 1].xcor()
            new_y = self.mytur[sum - 1].ycor()
            self.mytur[sum].goto(new_x, new_y)
        self.head.forward(20)






    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)




