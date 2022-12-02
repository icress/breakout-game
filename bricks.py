from turtle import Turtle


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=4, stretch_wid=2.5)

