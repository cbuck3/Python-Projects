from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def paddle_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
