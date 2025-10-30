#IC 1st turtle race

#import libraries
import turtle as turt
import random
import time
#define all colors
colors = ["magenta","red",'blue',"green","gold1","gray0","black","white"]
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
racer1.color("magenta"),racer2.color("red"),racer3.color("blue"),racer4.color("green"),racer5.color("gold1"),refturt.color("white")
#create screen
screen = turt.Screen()
screen.bgcolor("black")
#Put turtles on screen
racer1.teleport(-400,400)
racer2.teleport(-400,200)
racer3.teleport(-400,0)
racer4.teleport(-400,-200)
racer5.teleport(-400,-400)
refturt.teleport(500,700)
#Show title
screen.title("Turtle Race!")
#draw finish
refturt.right(90)
refturt.forward(1400)
refturt.right(90)
#countdown
time.sleep(1)
screen.title("3")
time.sleep(1)
screen.title("2")
time.sleep(1)
screen.title("1")
time.sleep(1)
screen.title("GO")
#Make a while loop for the turtle's movements
while True:
    #show who might win and is they need to keep moving
    if racer1.xcor() >= 500:
        screen.title("The pink turtle won!")
        break
    else:
        racer1.forward(random.randint(10,30))

    if racer2.xcor() >= 500:
        screen.title("The red turtle won!")
        break
    else:
        racer2.forward(random.randint(10,30))

    if racer3.xcor() >= 500:
        screen.title("The blue turtle won!")
        break
    else:
        racer3.forward(random.randint(10,30))

    if racer4.xcor() >= 500:
        screen.title("The green turtle won!")
        break
    else:
        racer4.forward(random.randint(10,30))
        
    if racer5.xcor() >= 500:
        screen.title("The yellow turtle won!")
        break
    else:
        racer5.forward(random.randint(10,30))