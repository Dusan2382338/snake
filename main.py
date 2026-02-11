from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(height=650, width=750)
screen.bgcolor("black")
screen.tracer(0)
starting_snake_length = 10
snake_tail = []

class SnakePart(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.current_position = None
        self.previous_position = None

def snake_go():
    for i in range (0, snake_length):
        if i == 0: #regulates movement of the head
            snake_tail[0].previous_position = snake_tail[0].current_position
            snake_tail[0].forward(20)
            x,y = snake_tail[0].pos()
            snake_tail[0].current_position = (round(x), round(y)) #because .pos returns float
        else: #regulates movement of the body
            snake_tail[i].previous_position = snake_tail[i].current_position
            snake_tail[i].goto(snake_tail[i-1].previous_position)
            x,y = snake_tail[i].pos()
            snake_tail[i].current_position = (round(x), round(y))
            whole_snake_position.append(snake_tail[i].previous_position)

def draw_borders():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    turtle.goto(x=340, y=300)
    turtle.pendown()
    turtle.goto(x=340, y=-300)
    turtle.goto(x=-340, y=-300)
    turtle.goto(x=-340, y=300)
    turtle.goto(x=340, y=300)

def spawn_food():
    food = SnakePart()
    food.color("red")
    food.goto(x=random.randrange(start=-320, stop=320, step=20), y=random.randrange(start=-280, stop=280, step=20))
    a,b = food.pos()
    food.current_position = (round(a), round(b))
    return food

def spawn_snake():
    turtle_size = 20
    for i in range(0,starting_snake_length):
        tail = SnakePart()
        snake_tail.append(tail)
        tail.goto(x=snake_tail[i].xcor()-turtle_size, y=tail.ycor())
        snake_tail[i].current_position = tail.pos()
        snake_tail[i].previous_position = tail.pos()
        turtle_size+=20

def collision():
    if snake_tail[0].current_position in whole_snake_position:
        screen.title("Snake hit itself, game over!")
        return True
    if snake_tail[0].current_position[0] > 320 or snake_tail[0].current_position[0] < -320:
        screen.title("Snake hit wall, game over!")
        return True
    if snake_tail[0].current_position[1] > 280 or snake_tail[0].current_position[1] < -280:
        screen.title("Snake hit wall, game over!")
        return True

def snake_up():
    if snake_tail[0].heading() != 270:
        snake_tail[0].setheading(90)
def snake_down():
    if snake_tail[0].heading() != 90:
        snake_tail[0].setheading(270)
def snake_left():
    if snake_tail[0].heading() != 0:
        snake_tail[0].setheading(180)
def snake_right():
    if snake_tail[0].heading() != 180:
        snake_tail[0].setheading(0)

screen.onkeypress(key="w", fun=snake_up)
screen.onkeypress(key="s", fun=snake_down)
screen.onkeypress(key="a", fun=snake_left)
screen.onkeypress(key="d", fun=snake_right)
screen.listen()

whole_snake_position = []
is_game_over = False
current_food = spawn_food()
draw_borders()
spawn_snake()
while not is_game_over:
    snake_length = len(snake_tail)
    screen.title(f"Snake length: {snake_length}")
    snake_go()
    if collision():
        is_game_over = True
        break
    if snake_tail[0].current_position == current_food.current_position:
        current_food.reset()
        new_tail = SnakePart()
        new_tail.goto(snake_tail[-1].previous_position)
        snake_tail.append(new_tail)
        snake_tail[-1].current_position = snake_tail[-1].previous_position
        current_food = spawn_food()
        screen.title(f"Snake length: {snake_length+1}")
    whole_snake_position = []
    screen.update()
    time.sleep(0.1)

screen.exitonclick()