import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Make a Bet", prompt="Choose a Color: ")

colors = ["green", "red", "violet", "pink", "blue", "black",]
y_pos = [120, 80, 40, 0, -40, -80]

is_race_on = False
all_tutles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_pos[i])
    all_tutles.append(tim)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_tutles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_choice:
                print(f"You Won! {win_color} turtle is a Winner. ")
            else:
                print(f"You Lose! {win_color} is a Winner. ")

        rand_num = random.randint(0, 6)
        turtle.forward(rand_num)




screen.exitonclick()

