from Color import Color
from math import ceil

class Hexagon:

    origin = None
    turtle = None
    hexagons = None
    hexagonRadius = None
    size = None
    x_offset = None
    y_offset = None


    # Constructor
    def __init__(self, i, j):
        self.color = Color.red
        self.i = i
        self.j = j

    # Static Methods

    @staticmethod
    def create_n_by_n_grid(n, radius = 10):
        Hexagon.size = n
        Hexagon.hexagons = [[None for i in range(0, n)] for i in range(0, n)]
        Hexagon.origin = [0, 0]
        Hexagon.hexagonRadius = radius
        for i in range(0, n):
            for j in range(0, n):
                Hexagon.hexagons[i][j] = Hexagon(i, j)

    @staticmethod
    def set_offsets():
        Hexagon.x_offset = Hexagon.hexagonRadius * ceil(10/6 * Hexagon.hexagonRadius)
        Hexagon.y_offset = 2 * Hexagon.hexagonRadius


    @staticmethod
    def draw_all():
        Hexagon.set_offsets()
        for i in range(0, Hexagon.size):
            for j in range(0, Hexagon.size):
                Hexagon.draw_hexagon(Hexagon.hexagons[i][j])

    @staticmethod
    def setTurtle(turtle):
        Hexagon.turtle = turtle

    @staticmethod
    def get_color_string(color):
        if color == Color.red:
            return "red"
        elif color == Color.blue:
            return "blue"
        else:
            return "white"

    @staticmethod
    def coordinates(hexagon):
        return [Hexagon.origin[0] + Hexagon.x_offset * 2 * hexagon.i, Hexagon.origin[1] + Hexagon.y_offset * hexagon.j]

    @staticmethod
    def get_x_y(hexagon):
        pos = [0, 0]
        pos[0] = ceil((hexagon.j * 5/6 + hexagon. i * 10/6) * Hexagon.hexagonRadius)
        pos[1] = -ceil(hexagon.j * 1.5 * Hexagon.hexagonRadius)
        return pos

    @staticmethod
    def draw_hexagon(hexagon):
        if Hexagon.turtle == None:
            return
        Hexagon.turtle.up()
        coordinates = Hexagon.get_x_y(hexagon)
        Hexagon.turtle.goto(coordinates[0], coordinates[1])
        Hexagon.turtle.down()
        Hexagon.turtle.dot()
        Hexagon.turtle.up()
        Hexagon.turtle.setheading(270)
        Hexagon.turtle.forward(Hexagon.hexagonRadius)
        Hexagon.turtle.setheading(30)
        Hexagon.turtle.down()
        col = Hexagon.get_color_string(hexagon.color)
        Hexagon.turtle.begin_fill()
        Hexagon.turtle.color(col, col)
        for i in range(0, 6):
            Hexagon.turtle.forward(Hexagon.hexagonRadius)
            Hexagon.turtle.left(60)
        Hexagon.turtle.end_fill()



    def getTurtle(self):
        return Hexagon.turtle

    @staticmethod
    def occupy(hexagon, color, draw = True):
        if color != Color.red and color != Color.blue and color != Color.blank:
            return
        else:
            hexagon.color = color
        if draw == True:
            Hexagon.draw_hexagon(hexagon)

    def draw(self):
        if Hexagon.turtle == None:
            return
        else:
            Hexagon.turtle.goto(0,0)
            Hexagon.turtle.goto(Hexagon.hexagonRadius, 0)
            Hexagon.turtle.left(30)
            color_string = Hexagon.get_color_string(self.color)
            Hexagon.turtle.color(color_string, color_string)
            Hexagon.turtle.begin_fill()


