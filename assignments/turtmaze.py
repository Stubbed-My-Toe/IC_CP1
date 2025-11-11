#IC 1st Maze generator py

#Import turtle as t
import turtle as t
#import random
import random
import time
#make screen and screen color
screen = t.Screen()
screen.setup(800,800)
screen.screensize(700,700)
screen.bgcolor("black")
#make maze turtle
turt = t.Turtle()
turt.shape("turtle")
turt.pencolor("white")
turt.color("white")
#Define turt start
startpoint = turt.teleport(-300,-300)
#define frame of maze which is 600x600 with 50px holes at 300x300 and -300x-300
def frame():
    turt.teleport(-300,-300)
    turt.penup()
    turt.forward(50)
    turt.pendown()
    turt.forward(550)
    turt.left(90)
    turt.forward(600)
    turt.left(90)
    turt.penup()
    turt.forward(50)
    turt.pendown()
    turt.forward(550)
    turt.left(90)
    turt.forward(600)


frame()
#def grid of maze.grid
ungrid =[" "," "," "," "," "," ",
        " "," "," "," "," "," ",
        " "," "," "," "," "," ",
        " "," "," "," "," "," ",
        " "," "," "," "," "," ",
        " "," "," "," "," "," "]

def grid_y():
    len(ungrid)
    print(len(ungrid))
    for x, y in ungrid:
        turt.teleport(startpoint)
        turt.forward(600)
        y
grid_y()


        
screen.exitonclick()
#if random.randint(1,2)==1:
#maze width and height needs to be defined at least a six by six, or 600x600

#Room for six paths to head straight down from top to bottom.
#room for six or more paths to go side to side
#1 == wall
#0 == path
#[      ,
#       ,
#       ,
#       ,]
#inside of maze needs to be defined
#grid_rows=[]
grid_rows=[]
grid_columns=[]
#grid_columns=[1,1,1,1,#you get the gist]
#Define start and end of maze
#start making turtle make maze
