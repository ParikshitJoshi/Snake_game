from turtle import Turtle
starting_positions = [(0, 0), (-21, 0), (-42, 0)]
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg_num - 1].xcor()
            y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x, y)
        self.segment[0].forward(move_distance)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(270)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(0)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(180)
