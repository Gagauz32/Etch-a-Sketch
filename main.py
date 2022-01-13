import turtle as t

tupa = t.Turtle()
screen = t.Screen()
screen.bgcolor("floralwhite")
tupa.color("red")
tupa.speed("fast")
tupa.shape("turtle")
tupa.shapesize(3)


def move_forward():
    tupa.forward(10)


def move_backward():
    tupa.back(10)


def turn_left():
    tupa.setheading(tupa.heading() + 10)


def turn_right():
    tupa.setheading(tupa.heading() - 10)


def restart_game():
    tupa.penup()
    tupa.setposition(0, 0)
    tupa.clear()
    tupa.setheading(0)
    tupa.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=restart_game)

screen.exitonclick()
