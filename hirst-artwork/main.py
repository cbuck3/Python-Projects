from turtle import Turtle
from turtle import Screen
import random

color_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235),
              (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
              (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87),
              (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172),
              (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210), (77, 37, 76),
              (120, 117, 155), (35, 35, 35)]

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed(0)


def random_color():
    new_color = random.choice(color_list)
    return new_color


tim.pu()
tim.setposition(-250, -250)
tim.hideturtle()


def draw_dots():
    for x in range(9):
        tim.pd()
        tim.dot(20, random_color())
        tim.pu()
        tim.forward(50)
        tim.dot(20, random_color())
        tim.pu()


def turn_west():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)


def turn_east():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


for x in range(5):
    draw_dots()
    turn_west()
    draw_dots()
    turn_east()

screen.exitonclick()
