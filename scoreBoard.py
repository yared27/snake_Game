from food import Turtle
ALIGNMENT="center"
FONT=('Arial',12,'normal')

class ScoreBoard(Turtle):
      def __init__(self):
          super().__init__()
          # self.shape("square")
          self.goto(0,280)
          self.color("white")
          self.hideturtle()
          self.score=0
          with open("data.txt") as data:
              self.high_score=int(data.read())
          self.print_score()

      def print_score(self):
          self.clear()
          self.write(f"Score:{self.score } High Score : { self.high_score} ", move=False,align=ALIGNMENT ,font=FONT)
          self.color()

      def reset_high_score(self):
          if self.score>self.high_score:
              print("done")
              self.high_score=self.score
              with open("data.txt",mode="w") as data:
                 data.write(f"{self.high_score}")
          self.score=0
          self.print_score()
      def increase_score(self):
           self.score += 1
           self.print_score()




      # def game_over(self):
      #     self.goto(x=-4,y=0)
      #     self.color("white")
      #     self.write("GAME OVER", move=False, align="center" ,font=('Arial', 15, 'normal'))

