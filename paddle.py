from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('skyblue')
        self.shapesize(stretch_wid=1, stretch_len=12)

    def move_right(self):
        self.goto(y=self.ycor(), x=self.xcor() + 20)

    def move_left(self):
        self.goto(y=self.ycor(), x=self.xcor() - 20)

