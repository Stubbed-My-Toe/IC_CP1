#IC 1st Maze generator py


#I'm sorry but I don't know how to do this, and after many attempts I still cannot figure it out.
#Even with help from you, others and the internet, I did not know what to do. I have failed this assignment.
#I will work harder on this coding class





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
grid_rows=[[0,5],[0,4],[0.3],[0,2],[0,1],[0,0],
           [1,0],[1,1],[1,2],[1,3],[1,4],[1,5],
           [2,5],[2,4],[2,3],[2,2],[2,1],[2,0],
           [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],
           [4,5],[4,4],[4,3],[4,2],[4,1],[4,0],
           [5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]
grid_columns=[[0,0],[5,1],[0,2],[5,3],[0,4],[5,5],
              [1,0],[4,1],[1,2],[4,3],[1,4],[4,5],
              [2,0],[3,1],[2,2],[3,3],[2,4],[3,5],
              [3,0],[2,1],[3,2],[2,3],[3,4],[2,5],
              [4,0],[1,1],[4,2],[1,3],[4,4],[1,5],
              [5,0],[0,1],[5,2],[0,3],[5,4],[0,5]]

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
