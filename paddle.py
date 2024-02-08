from turtle import Turtle


class Paddle(Turtle):
    """Doc string for Paddle in the breakout game. The paddlw has attributes of shape-which is a 'square' of Turtle, a color of 'white', a shapesize which defines the form the paddle will take, and a goto, for the position of the paddle on the x and y axis of the screen"""

    def __init__(self, go_to):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(go_to)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
