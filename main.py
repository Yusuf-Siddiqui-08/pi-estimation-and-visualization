import math
import turtle
from decimal import *
from turtle import *
from turtle import Screen

mode("logo")
title("Pi Estimation and Visualization")
screen = Screen()
screen.setup(720, 720)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)

px2cm = 0.0264583333


def init(setN=False):
    global n, r, angle
    if setN is not False and setN >= 3:
        n = setN
    else:
        n = 3
    r = 150
    angle = 360 / n


def getPositions(_angle, _n, _r):
    _positions = []
    t.penup()
    t.setheading(0 - angle)
    for side in range(_n):
        t.goto(0, 0)
        t.forward(_r)
        t.right(_angle)
        _positions.append(t.pos())
    t.goto(_positions[0][0], _positions[0][1])
    return {"positions": _positions}


def calculateAreas(polySideLength):
    A = angle / 2
    polygonApothem = r * math.cos(math.radians(A))
    polygonArea = n * ((polySideLength * polygonApothem) / 2)
    piEstimate = polygonArea / (r ** 2)
    _areaInfo = {"actual circle area": Decimal((math.pi * (r ** 2))),  # pi * radius squared
                 "polygon area": Decimal(polygonArea),
                 "pi estimate": Decimal(piEstimate)}
    return _areaInfo


def drawVizualization():
    t.penup()
    t.clear()
    t.goto(0, 0)
    t.dot(5, "black")
    info = getPositions(angle, n, r)
    positions = info["positions"]
    start = positions[0]
    t.begin_poly()
    for pos in positions:
        t.pendown()
        t.goto(pos[0], pos[1])
    s = t.distance(start[0], start[1])
    t.goto(start[0], start[1])
    t.end_poly()
    t.penup()
    t.goto((0 + r), 0)
    t.setheading(0)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(0, -300)
    t.write("Don't spam the controls!"
            "\nPress R to reset. "
            "\nPress Q to quit. "
            "\nLeft-Click to increase the number of sides."
            "\nRight-Click to decrease the number of sides.",
            False, align="center", font=("Arial", 12, "normal"))
    areaInfo = calculateAreas(s)
    t.goto(-300, 200)
    t.write(
        "Actual Area (area of circle using pi): " + str(areaInfo["actual circle area"] * Decimal(px2cm) ** 2) + "cm²"
            "\n\nNumber of sides on the polygon: " + str(n) +
            "\nArea of polygon (without using pi): " + str(areaInfo["polygon area"] * Decimal(px2cm) ** 2) + "cm²"
            "\n\nPi Estimation: " + str(areaInfo["pi estimate"]) +
            "\nPi Estimation Error: " + str(Decimal(math.pi) - areaInfo["pi estimate"]),
        False, align="left", font=("Arial", 12, "normal"))
    t.penup()


def clickLeft(x, y):
    _n = n
    _n += 1
    init(_n)
    execMain(False)


def clickRight(x, y):
    _n = n
    _n -= 1
    init(_n)
    execMain(False)


def execMain(_init: bool = True):
    t.clear()
    t.goto(0,0)
    t.penup()
    if _init:
        init()
    drawVizualization()
    screen.onkeypress(execMain, "r")
    screen.onkeypress(exit, "q")
    screen.onscreenclick(clickLeft, 1)
    screen.onscreenclick(clickRight, 3)


def exit():
    quit()


execMain(True)

screen.listen()

screen.mainloop()
