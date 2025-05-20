from turtle import *
import colorsys

bgcolor('black')
speed(0)
h = 0.0


def draw():
    global h
    for i in range(300):
        h += 0.015
        c = colorsys.hsv_to_rgb(h % 1, 1, 1)
        pencolor(c)
        fillcolor(c)

        circle(190 - i, 90)
        left(90)
        circle(190 - i, 90)
        left(18)


draw()
done()