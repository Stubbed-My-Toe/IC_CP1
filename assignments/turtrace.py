#IC 1st turtle race

#import libraries
import turtle as turt
import random
import time
#define all colors
colors = ["black","red",'blue',"green","gold1","gray0"]
#create turtles
refturt = turt.Turtle()
racer1 = turt.Turtle()
racer2 = turt.Turtle()
racer3 = turt.Turtle()
racer4 = turt.Turtle()
racer5 = turt.Turtle()
#create turtle shape
racer1.shape("turtle"),racer2.shape("turtle"),racer3.shape("turtle"),racer4.shape("turtle"),racer5.shape("turtle"),refturt.shape("turtle")
#color turt
racer1.color("black"),racer2.color("red"),racer3.color("blue"),racer4.color("green"),racer5.color("gold1")
#create screen
screen = turt.Screen()
#Put turtles on screen
racer1.teleport(-400,200)
racer2.teleport(-400,100)
racer3.teleport(-400,0)
racer4.teleport(-400,-100)
racer5.teleport(-400,-200)
refturt.teleport(500,300)
#Show title
screen.title("Turtle Race!")
#countdown
time.sleep(1)
screen.title("3")
time.sleep(1)
screen.title("2")
time.sleep(1)
screen.title("1")
time.sleep(1)
screen.title("GO")
refturt.right
refturt.forward(600)
while True:
