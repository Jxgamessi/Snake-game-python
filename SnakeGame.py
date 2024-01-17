import turtle
import time
import random

delay = 0.1

ssk = turtle.Screen()
ssk.title("SNAKE AND SNACK")
ssk.bgcolor("black")
ssk.setup(width=1000, height=800)
ssk.tracer(0)


grid = turtle.Turtle()
grid.speed(0)
grid.color("red")
grid.penup()
grid.hideturtle()
grid.goto(-290, -190)
grid.pendown()
for _ in range(2):
    grid.forward(580)
    grid.left(90)
    grid.forward(380)
    grid.left(90)

jp = turtle.Turtle()
jp.speed(0)
jp.shape("triangle")
jp.color("cyan")
jp.penup()
jp.goto(0, 0)
jp.direction = "Right"

fp = turtle.Turtle()
fp.speed(0)
fp.shape("circle")
fp.color("yellow")
fp.penup()
fp.goto(0, 100)

rrr = []

px = turtle.Turtle()
px.speed(0)
px.color("white")
px.penup()
px.hideturtle()
px.goto(0, 180)
px.write("Score: 0", align="center", font=("Courier", 20, "normal"))

def move_up():
    if jp.direction != "Down":
        jp.direction = "Up"

def move_down():
    if jp.direction != "Up":
        jp.direction = "Down"

def move_left():
    if jp.direction != "Right":
        jp.direction = "Left"

def move_right():
    if jp.direction != "Left":
        jp.direction = "Right"

def move_snake():
    if jp.direction == "Up":
        y = jp.ycor()
        jp.sety(y + 20)

    if jp.direction == "Down":
        y = jp.ycor()
        jp.sety(y - 20)

    if jp.direction == "Left":
        x = jp.xcor()
        jp.setx(x - 20)

    if jp.direction == "Right":
        x = jp.xcor()
        jp.setx(x + 20)

ssk.listen()
ssk.onkeypress(move_up, "Up")
ssk.onkeypress(move_down, "Down")
ssk.onkeypress(move_left, "Left")
ssk.onkeypress(move_right, "Right")

game_score = 0
while True:
    ssk.update()

    if (
        jp.xcor() > 270
        or jp.xcor() < -270
        or jp.ycor() > 170
        or jp.ycor() < -170
    ):
        time.sleep(1)
        jp.goto(0, 0)
        jp.direction = "Right"
        for segment in rrr:
            segment.goto(1000, 1000)
        rrr.clear()
        game_score = 0
        delay = 0.1
        px.clear()
        px.write("Score: {}".format(game_score), align="center", font=("Courier", 16, "normal"))

    if jp.distance(fp) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-170, 170)
        fp.goto(x, y)

        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.color("white")
        ns.penup()
        rrr.append(ns)

        delay -= 0.001

        game_score += 10
        px.clear()
        px.write("Score: {}".format(game_score), align="center", font=("Courier", 16, "normal"))

    for index in range(len(rrr) - 1, 0, -1):
        x = rrr[index - 1].xcor()
        y = rrr[index - 1].ycor()
        rrr[index].goto(x, y)

    if len(rrr) > 0:
        x = jp.xcor()
        y = jp.ycor()
        rrr[0].goto(x, y)

    move_snake()

    for segment in rrr:
        if jp.distance(segment) < 20:
            time.sleep(1)
            jp.goto(0, 0)
            jp.direction = "Right"
            for segment in rrr:
                segment.goto(1000, 1000)
            rrr.clear()
            game_score = 0
            delay = 0.1
            px.clear()
            px.write("Score: {}".format(game_score), align="center", font=("Courier", 16, "normal"))

    time.sleep(delay)
