from turtle import Screen
from snake_class import Snake
from food import Turtle
from scoreBoard import ScoreBoard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Turtle()
scoreB=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on=True

while is_game_on:

   screen.update()
   time.sleep(0.1)
   snake.snake_fun()

   if snake.head.distance(food)<15:
      scoreB.increase_score()
      snake.extend()
      scoreB.print_score()
      food.refresh()

   # check if the head reaches the screen
   if snake.head.xcor()>292 or snake.head.xcor()<-292 or snake.head.ycor()>300 or snake.head.ycor()<-290:
      scoreB.reset_high_score()
      snake.reset_snake()
   for senakes in snake.turtles[1:]:
      if snake.head.distance(senakes)<10:
         scoreB.reset_high_score()
         snake.reset_snake()
screen.exitonclick()
