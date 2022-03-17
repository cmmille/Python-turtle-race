import turtle as t
import random


def init_turtles(track_size):
    red_t = t.Turtle(shape="turtle")
    purple_t = t.Turtle(shape="turtle")
    blue_t = t.Turtle(shape="turtle")
    green_t = t.Turtle(shape="turtle")
    yellow_t = t.Turtle(shape="turtle")

    # Set colors
    red_t.color("red")
    blue_t.color("blue")
    green_t.color("green")
    purple_t.color("purple")
    yellow_t.color("yellow")

    turtles = [red_t, purple_t, blue_t, green_t, yellow_t]

    # Move to starting line
    vert_pos = -160
    for turtle in turtles:
        turtle.penup()
        turtle.shapesize(2.5)
        turtle.setposition(track_size / -2 + 20, vert_pos)
        turtle.speed("normal")
        vert_pos += 80

    return turtles


def move_turtle(turtle):
    rand_step = random.randint(1, 10)
    turtle.forward(rand_step)


def move_rand_turtle(turtles):
    rand_turtle = random.choice(turtles)
    move_turtle(rand_turtle)


def start_race(track_size):
    screen = t.Screen()
    screen.setup(width=track_size, height=400)
    user_bet = screen.textinput("Who will win?", "Red, purple, blue, green, or yellow?").capitalize()
    turtles = init_turtles(track_size)

    race_over = False
    while not race_over:
        move_rand_turtle(turtles)
        for turtle in turtles:
            if turtle.xcor() > track_size / 2 -40:
                winning_color = turtle.color()[0].capitalize()
                result = f"{winning_color} turtle wins!"
                if user_bet == winning_color:
                    result+="\nYou win!"
                else:
                    result+="\nYou lose!"
                screen.textinput("Race results", result)
                race_over = True

    screen.exitonclick()


start_race(800)
