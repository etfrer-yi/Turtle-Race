from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
# Note: coordinate system has origin right in the middle
# Splits the width and the height exactly in half
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x=-230, y=20)

tom = Turtle(shape="turtle")
tom.penup()
tom.goto(x=-230, y=-20)

tem = Turtle(shape="turtle")
tem.penup()
tem.goto(x=-230, y=40)

tam = Turtle(shape="turtle")
tam.penup()
tam.goto(x=-230, y=-40)

timmy = Turtle(shape="turtle")
timmy.penup()
timmy.goto(x=-230, y=60)

tammy = Turtle(shape="turtle")
tammy.penup()
tammy.goto(x=-230, y=-60)

colors = ["blue", "dark green", "red", "yellow", "orange", "spring green"]
turtles = [tim, tom, tem, tam, timmy, tammy]
for _ in range(len(turtles)):
    turtles[_].color(colors[_])

winning_turtle = ""
no_winner = True
while no_winner:
    for turtle in turtles:
        turtle.forward(randint(15, 50))
    for turtle in turtles:
        if (turtle.position()[0] >= 200):
            no_winner = False
            winning_turtle += turtle.__str__()

if (winning_turtle == user_bet):
    print(f'Yes! {user_bet} is indeed the winner!')
else:
    print(f"Nope! {user_bet} is not the winner.")


screen.exitonclick()