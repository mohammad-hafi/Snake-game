from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_in=screen.textinput(title="choose a color",prompt="which color will win the race?guess!!: ")
turtle_color=["red","blue","green","yellow","purple","black"]
yais=[-100,-75,-50,-25,-0,25]
turtlesarry=[]
for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(turtle_color[i])
    tim.goto(x=-230,y=yais[i])
    turtlesarry.append(tim)

if user_in:
    start_race=True

while start_race:
    for turtles in turtlesarry:
        randdis=random.randint(0,10)
        turtles.forward(randdis)
        if turtles.xcor()>230:
            start_race=False
            winner=turtles.pencolor()
            if winner==user_in:
                print(f"you won the race!! The {winner} reached first")
            else:
                print(f"you lost the race!! The {winner} reached first")
















screen.exitonclick()


