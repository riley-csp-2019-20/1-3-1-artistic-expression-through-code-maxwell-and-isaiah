# Import assets
import turtle as trtl
import random as rdm
# define variables
repeat_amount = 55
move_dist = 50
gap_size = 25
coin_amount = 0
points = 0
collision=False
# set background color
wn = trtl.Screen()
wn.bgcolor("grey")

# tell the user the controls
print("--Controls--")
print("W - move up")
print("S - move down")
print("D - move right")
print("A - move left")

# define turtles
drawmaze = trtl.Turtle()
coin_1 = trtl.Turtle()
player = trtl.Turtle()

# set Turtle settings
drawmaze.pencolor("aqua")
drawmaze.pensize(5)
drawmaze.left(90)
drawmaze.goto(0,0)
drawmaze.ht()
drawmaze.speed(0)
player.penup()
player.ht()
player.shape("turtle")
player.shapesize(.8)
player.color("green")
player.goto(-40,40)
player.speed(0)

# Define Functions
def botup():
    global collision
    global points
    player.setheading(90)
    player.forward(10)
    if (player.distance(coin_1.xcor(), coin_1.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_2.xcor(), coin_2.ycor()) < 10):
        collision=True
        points += 1
        coin_2.ht()
        print(points)
        collision=False
    if (player.distance(coin_3.xcor(), coin_3.ycor()) < 10):
        collision=True
        points += 1
        coin_3.ht()
        print(points)
        collision=False
    if (player.distance(coin_4.xcor(), coin_4.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_5.xcor(), coin_5.ycor()) < 10):
        collision=True
        points += 1
        coin_5.ht()
        print(points)
        collision=False
    if (player.distance(coin_6.xcor(), coin_6.ycor()) < 10):
        collision=True
        points += 1
        coin_6.ht()
        print(points)
        collision=False
    if (player.distance(coin_7.xcor(), coin_7.ycor()) < 10):
        collision=True
        points += 1
        coin_7.ht()
        print(points)
        collision=False
    if (player.distance(coin_8.xcor(), coin_8.ycor()) < 10):
        collision=True
        points += 1
        coin_8.ht()
        print(points)
        collision=False


def botright():
    global collision
    global points
    player.setheading(0)
    player.forward(10)
    if (player.distance(coin_1.xcor(), coin_1.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_2.xcor(), coin_2.ycor()) < 10):
        collision=True
        points += 1
        coin_2.ht()
        print(points)
        collision=False
    if (player.distance(coin_3.xcor(), coin_3.ycor()) < 10):
        collision=True
        points += 1
        coin_3.ht()
        print(points)
        collision=False
    if (player.distance(coin_4.xcor(), coin_4.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_5.xcor(), coin_5.ycor()) < 10):
        collision=True
        points += 1
        coin_5.ht()
        print(points)
        collision=False
    if (player.distance(coin_6.xcor(), coin_6.ycor()) < 10):
        collision=True
        points += 1
        coin_6.ht()
        print(points)
        collision=False
    if (player.distance(coin_7.xcor(), coin_7.ycor()) < 10):
        collision=True
        points += 1
        coin_7.ht()
        print(points)
        collision=False
    if (player.distance(coin_8.xcor(), coin_8.ycor()) < 10):
        collision=True
        points += 1
        coin_8.ht()
        print(points)
        collision=False

def botdown():
    global collision
    global points
    player.setheading(270)
    player.forward(10)
    if (player.distance(coin_1.xcor(), coin_1.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_2.xcor(), coin_2.ycor()) < 10):
        collision=True
        points += 1
        coin_2.ht()
        print(points)
        collision=False
    if (player.distance(coin_3.xcor(), coin_3.ycor()) < 10):
        collision=True
        points += 1
        coin_3.ht()
        print(points)
        collision=False
    if (player.distance(coin_4.xcor(), coin_4.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_5.xcor(), coin_5.ycor()) < 10):
        collision=True
        points += 1
        coin_5.ht()
        print(points)
        collision=False
    if (player.distance(coin_6.xcor(), coin_6.ycor()) < 10):
        collision=True
        points += 1
        coin_6.ht()
        print(points)
        collision=False
    if (player.distance(coin_7.xcor(), coin_7.ycor()) < 10):
        collision=True
        points += 1
        coin_7.ht()
        print(points)
        collision=False
    if (player.distance(coin_8.xcor(), coin_8.ycor()) < 10):
        collision=True
        points += 1
        coin_8.ht()
        print(points)
        collision=False

def botleft():
    global collision
    global points
    player.setheading(180)
    player.forward(10)
    if (player.distance(coin_1.xcor(), coin_1.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_2.xcor(), coin_2.ycor()) < 10):
        collision=True
        points += 1
        coin_2.ht()
        print(points)
        collision=False
    if (player.distance(coin_3.xcor(), coin_3.ycor()) < 10):
        collision=True
        points += 1
        coin_3.ht()
        print(points)
        collision=False
    if (player.distance(coin_4.xcor(), coin_4.ycor()) < 10):
        collision=True
        points += 1
        coin_1.ht()
        print(points)
        collision=False
    if (player.distance(coin_5.xcor(), coin_5.ycor()) < 10):
        collision=True
        points += 1
        coin_5.ht()
        print(points)
        collision=False
    if (player.distance(coin_6.xcor(), coin_6.ycor()) < 10):
        collision=True
        points += 1
        coin_6.ht()
        print(points)
        collision=False
    if (player.distance(coin_7.xcor(), coin_7.ycor()) < 10):
        collision=True
        points += 1
        coin_7.ht()
        print(points)
        collision=False
    if (player.distance(coin_8.xcor(), coin_8.ycor()) < 10):
        collision=True
        points += 1
        coin_8.ht()
        print(points)
        collision=False

# Draw the maze
for i in range(repeat_amount):
    if i > 4:
        door = rdm.randint(gap_size, (move_dist - gap_size))
        drawmaze.forward(door)
        drawmaze.penup()
        drawmaze.forward(gap_size)
        drawmaze.pendown()
        drawmaze.left(90)

        # Make the Walls and Gaps
        drawmaze.forward(gap_size)
        drawmaze.back(gap_size)
        drawmaze.right(90)
        drawmaze.forward(move_dist - gap_size - door)
        drawmaze.left(90)
        move_dist +=15    
 


# Add coins to the maze
coin_1 = trtl.Turtle()
coin_1.ht()
coin_1.penup()
coin_1.shape("circle")
coin_1.shapesize(.5)
coin_1.color("yellow")
coin_1.speed(0)
coin_1.goto(200,200)
coin_1.st()

coin_2 = trtl.Turtle()
coin_2.ht()
coin_2.penup()
coin_2.shape("circle")
coin_2.shapesize(.5)
coin_2.color("yellow")
coin_2.speed(0)
coin_2.goto(170,-100)
coin_2.st()

coin_3 = trtl.Turtle()
coin_3.ht()
coin_3.penup()
coin_3.shape("circle")
coin_3.shapesize(.5)
coin_3.color("yellow")
coin_3.speed(0)
coin_3.goto(-300,50)
coin_3.st()

coin_4 = trtl.Turtle()
coin_4.ht()
coin_4.penup()
coin_4.shape("circle")
coin_4.shapesize(.5)
coin_4.color("yellow")
coin_4.speed(0)
coin_4.goto(400,-70)
coin_4.st()
        
coin_5 = trtl.Turtle()
coin_5.ht()
coin_5.penup()
coin_5.shape("circle")
coin_5.shapesize(.5)
coin_5.color("yellow")
coin_5.speed(0)
coin_5.goto(-250,150)
coin_5.st()        

coin_6 = trtl.Turtle()
coin_6.ht()
coin_6.penup()
coin_6.shape("circle")
coin_6.shapesize(.5)
coin_6.color("yellow")
coin_6.speed(0)
coin_6.goto(250,350)
coin_6.st() 

coin_7 = trtl.Turtle()
coin_7.ht()
coin_7.penup()
coin_7.shape("circle")
coin_7.shapesize(.5)
coin_7.color("yellow")
coin_7.speed(0)
coin_7.goto(150,-350)
coin_7.st()

coin_8 = trtl.Turtle()
coin_8.ht()
coin_8.penup()
coin_8.shape("circle")
coin_8.shapesize(.5)
coin_8.color("yellow")
coin_8.speed(0)
coin_8.goto(225,112)
coin_8.st()

# Setup player movement
player.st()
wn.onkeypress(botup,"w")
wn.onkeypress(botright,"d")
wn.onkeypress(botdown,"s")
wn.onkeypress(botleft,"a")

wn.listen()
wn.mainloop()