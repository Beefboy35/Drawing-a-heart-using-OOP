import turtle, time
from typing import Union


class Shapes:

    def __init__(self, x: Union[int, float]):
        self.var = x

    def draw_heart(self, n: int):
        while n != 0:
            tur = turtle.Screen()

            tur.bgcolor("cyan")
            turt = turtle.Turtle()

            turt.color("red")
            tut = turtle.Screen()
            turtle.speed(10)
            turtle.left(45)
            turtle.forward(self.var)
            turtle.circle(self.var / 2, 180)
            turtle.right(90)
            turtle.circle(self.var / 2, 180)
            turtle.forward(self.var)
            time.sleep(1)
            turtle.clearscreen()
            n -= 1
        return "Thank you!"


Heart = Shapes(300)

print(Heart.draw_heart(2))
turtle.bye()
