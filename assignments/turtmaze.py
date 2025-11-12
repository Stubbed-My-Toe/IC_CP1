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
#define frame of maze which == 600x600 with 50px holes at 300x300 and -300x-300
#def frame():
    #turt.pendown()
    #turt.forward(550)
    #turt.left(90)
    #turt.forward(600)
    #turt.left(90)
    #turt.penup()
    #turt.forward(50)
    #turt.pendown()
    #turt.forward(550)
    #turt.left(90)
    #turt.forward(600)


#frame()
#def grid of maze.grid
grid_rows=[["1", "", "", "", "", "", "", "1"], 
           ["1", "", "", "", "", "", "", "1"], 
           ["1", "", "", "", "", "", "", "1"], 
           ["1", "", "", "", "", "", "", "1"], 
           ["1", "", "", "", "", "", "", "1"], 
           ["1", "", "", "", "", "", "", "1"]]

grid_columns=[["0", "", "", "", "", "", "", "1"], 
              ["1", "", "", "", "", "", "", "1"], 
              ["1", "", "", "", "", "", "", "1"], 
              ["1", "", "", "", "", "", "", "1"], 
              ["1", "", "", "", "", "", "", "1"], 
              ["1", "", "", "", "", "", "", "0"]]


for x, row in enumerate(grid_rows):
    for y, cell in enumerate(row):
        if cell == "":
            grid_rows[x][y] = random.choice(["0","1"])

for y, column in enumerate(grid_columns):
    for x, cell in enumerate(column):
        if cell == "":
            grid_columns[y][x] = random.choice(["0","1"])

turt.penup()
for x, row in enumerate(grid_rows):
    for y, cell in enumerate(row):
        if cell == "1":
            turt.goto(x*20-200,y*20-200)
            turt.setheading(90)
            turt.pendown()
            turt.forward(20)
            turt.penup()
for y, columns in enumerate(grid_columns):
    for x, cell in enumerate(columns):
        if cell == "1":
            turt.goto(x*20-200,y*20-200)
            turt.setheading(0)
            turt.pendown()
            turt.forward(20)
            turt.penup()
            

        
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

#grid_columns=[1,1,1,1,#you get the g==t]
#Define start and end of maze
#start making turtle make maze
