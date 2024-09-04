import math
import turtle
from decimal import *
from turtle import *
from turtle import Screen

px2cm = 0.0264583333

#COLOUR CONSTANTS
BG = "#1D4A5D"
POLYGON = "#C26ED1"
CIRCLE = "#531D5D"
TEXT = "#1FFFC7"
DOT = "#1B0C1D"

mode("logo")
title("Pi Estimation and Visualization")
screen = Screen()
screen.setup(720, 720)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)
turtle.bgcolor(BG)

rendering = False

def init(setN=False):
    global n, r, angle
    if setN is not False and setN >= 3:
        n = setN
    else:
        n = 3
    r = 150
    angle = 360 / n


def askN():
    n = turtle.textinput("Enter the number of sides:", "Number of sides on polygon: ")
    execMain(True, int(n))

def getPositions(_angle, _n, _r):
    _positions = []
    t.penup()
    t.setheading(0 - angle)
    for side in range(_n):
        t.goto(0, 0)
        t.forward(_r)
        t.right(_angle)
        _positions.append(t.pos())
    return  _positions


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
    rendering = True
    t.penup()
    t.clear()
    t.goto(0,0)
    t.color(TEXT)
    t.write("Loading...", move=False, align="center", font=("Arial", 50, "bold"))
    info = getPositions(angle, n, r)
    # render circle
    t.clear()
    t.color(CIRCLE)
    t.begin_fill()
    t.goto((0 + r), 0)
    t.setheading(0)
    t.pendown()
    t.circle(r)
    t.end_fill()
    t.penup()
    # render polygon
    positions = info
    start = positions[0]
    t.penup()
    t.goto(start[0], start[1])
    t.begin_poly()
    t.color(POLYGON)
    t.begin_fill()
    for pos in positions:
        t.pendown()
        t.goto(pos[0], pos[1])
    s = t.distance(start[0], start[1])
    t.goto(start[0], start[1])
    t.end_poly()
    polygon = t.get_poly()
    turtle.register_shape("polygon", polygon)
    t.end_fill()
    t.penup()
    # render text
    t.color(TEXT)
    t.goto(0, -300)
    t.write("Don't spam the controls!"
            "\nPress R to reset. "
            "\nPress Q to quit. "
            "\nPress E to enter number of sides. "
            "\nLeft-Click to increase the number of sides."
            "\nRight-Click to decrease the number of sides.",
            False, align="center", font=("Arial", 12, "normal"))
    areaInfo = calculateAreas(s)
    t.goto(-300, 300)
    t.setheading(0)
    spacing = 20
    t.color(CIRCLE)
    t.write("Actual Area (area of circle using pi): " + str(areaInfo["actual circle area"] * Decimal(px2cm) ** 2) + "cm²", False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(TEXT)
    t.write("Number of sides on the polygon: " + str(n), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(POLYGON)
    t.write("Area of polygon (without using pi): " + str(areaInfo["polygon area"] * Decimal(px2cm) ** 2) + "cm²", False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.color(TEXT)
    t.write("Pi Estimation: " + str(areaInfo["pi estimate"]), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.write("Pi Estimation Error: " + str(Decimal(math.pi) - areaInfo["pi estimate"]), False, align="left", font=("Arial", 12, "bold"))
    t.forward(-spacing)
    t.penup()
    # render center dot
    t.goto(0, 0)
    t.dot(5, DOT)
    rendering = False


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


def execMain(_init: bool = True, setN = False):
    t.clear()
    t.goto(0, 0)
    t.penup()
    if _init:
        init(setN)
    drawVizualization()
    screen.onkeypress(execMain, "r")
    screen.onkeypress(exit, "q")
    if not rendering:
        screen.onkeypress(askN, "e")
        screen.onscreenclick(clickLeft, 1)
        screen.onscreenclick(clickRight, 3)


def exit():
    quit()


execMain(True)

screen.listen()

screen.mainloop()
