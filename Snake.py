from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        x_cord = 0
        for _ in range(0, 3):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.setposition(x_cord, 0)
            self.segments.append(segment)
        x_cord -= 20
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.setposition(self.segments[-1].position())
        self.segments.append(segment)
