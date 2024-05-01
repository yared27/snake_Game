from turtle import Turtle, Screen
import time
UP=90
DOWN=270
RIGHT=0
LEFT=180
X = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    #
    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)
    def create_snake(self):
        for i in X:
            self.add_segment(i)

    def __init__(self):
        self.turtles = []
        self.screen = Screen()
        self.create_snake()
        self.head=self.turtles[0]

    def extend(self):
            self.add_segment(self.turtles[-1].position())

#to the square as a one pices of object
    def snake_fun(self):
            for turtle_num in range(len(self.turtles) - 1, 0, -1):
                new_x = self.turtles[turtle_num - 1].xcor()
                new_y = self.turtles[turtle_num - 1].ycor()
                self.turtles[turtle_num].goto(new_x, new_y)
            self.head.forward(20)

    #to move the snake upward
    def up(self):
        if self.head.heading()!=270:
          self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
           self.head.setheading(270)
    def right(self):
        if self.head.heading()!=180:
           self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def reset_snake(self):
        for i in self.turtles:
          i.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

        # self.snake_fun()