from turtle import Turtle, Screen
import random

COLOR_LIST = ["purple", "green", "blue", "white", "orange", "red"]
random_moves = [0, 5, 10, 15, 20, 25, 30]
screen = Screen()
screen.bgcolor("black")
user_bet = screen.textinput(title="Place your bet!", prompt="Choose color who will win!")
turtle_objects_list = [Turtle(shape="turtle") for i in range(len(COLOR_LIST))]
x, y = -280, -240

def turtle_move():
    return random.choice(random_moves)
def start_race():
    while True:
        for t in turtle_objects_list:
            t.forward(turtle_move())
            if t.xcor() > 280:
                return t.color()[0]

for i in range(len(turtle_objects_list)):
    turtle_objects_list[i].penup()
    turtle_objects_list[i].color(COLOR_LIST[i])
    turtle_objects_list[i].goto(x, y)
    y += 100

winner = start_race().title()
turtle_write = Turtle()
turtle_write.penup()
turtle_write.hideturtle()
turtle_write.color(winner)
turtle_write.write(f"Congratulations!! {winner} turtle wins the race.", align="center", font=('Arial', 24, "normal")) if winner == user_bet else turtle_write.write(f"Oh!! {winner} turtle wins the race.", align="center", font=('Arial', 24, "normal"))
screen.exitonclick()
