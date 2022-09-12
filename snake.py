import turtle as t

block_position = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.initial_body = []
        self.creating_snake_body()
        self.head = self.initial_body[0]
        self.head.color('purple')

    def creating_snake_body(self):
        for block in block_position:
            snake_body_part = t.Turtle(shape='square')
            snake_body_part.color('white')
            snake_body_part.penup()
            snake_body_part.goto(block)
            self.initial_body.append(snake_body_part)

    def moving_snake(self):
        for block in range(len(self.initial_body) - 1, 0, -1):
            xfactor = self.initial_body[block - 1].xcor()
            yfactor = self.initial_body[block - 1].ycor()
            self.initial_body[block].goto(x=xfactor, y=yfactor)
        self.initial_body[0].forward(20)

    def snake_ate_food(self):
        new_block = t.Turtle(shape='square')
        new_block.color('white')
        new_block.penup()
        new_block.goto(self.initial_body[len(self.initial_body) - 1].position())
        self.initial_body.append(new_block)

    def game_pause(self):
        for block in (len(self.initial_body) - 1, 0, -1):
            self.initial_body[block].speed(0)

    def game_play(self):
        self.initial_body[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)