from turtle import *
from Hexagon import Hexagon

t = Turtle()
t.hideturtle()
t.speed = 0

Hexagon.create_n_by_n_grid(5, 40)
Hexagon.setTurtle(t)
Hexagon.draw_all()