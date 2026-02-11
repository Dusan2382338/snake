from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(height=650, width=750)
screen.bgcolor("black")
screen.tracer(0)
starting_snake_length = 10
snake_tail = []
turtle_size = 20

class SnakePart(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.current_position = None
        self.previous_position = None

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
    # Turtle(shape="square")
    # food.penup()
    food.color("red")
    food.goto(x=random.randrange(start=-320, stop=320, step=20), y=random.randrange(start=-280, stop=280, step=20))
    a,b = food.pos()
    food.current_position = (round(a), round(b))
    return food

for i in range(0,starting_snake_length):
    tail = SnakePart()
    # tail.penup()
    # tail.color("white")
    snake_tail.append(tail)
    tail.goto(x=snake_tail[i].xcor()-turtle_size, y=tail.ycor())
    snake_tail[i].current_position = tail.pos()
    snake_tail[i].previous_position = tail.pos()
    turtle_size+=20

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

while not is_game_over:

    snake_length = len(snake_tail)
    screen.title(f"Snake length: {snake_length}")

    for i in range (0, snake_length):
        if i == 0: #regulates movement of the head
            snake_tail[0].previous_position = snake_tail[0].current_position
            snake_tail[0].forward(20)
            x,y = snake_tail[0].pos() #because .pos() returns floats, have to round them
                                      #to integers
                                      #otherwise head and tail positions will not be same
                                      #because 20.0000001 != 20.000000 but 20 = 20
            snake_tail[0].current_position = (round(x), round(y))#see previous comment
        else: #regulates movement of the rest of the body
            snake_tail[i].previous_position = snake_tail[i].current_position
            snake_tail[i].goto(snake_tail[i-1].previous_position)
            x,y = snake_tail[i].pos()
            snake_tail[i].current_position = (round(x), round(y)) #see previous comment
            whole_snake_position.append(snake_tail[i].previous_position)
            #see previous comment
            #also, capture previous position, not current,
            #beacuse head hits the body before the body moves not after
    if snake_tail[0].current_position in whole_snake_position:
        screen.title("Game over, snake ate its tail")
        is_game_over = True
        # break
    if snake_tail[0].current_position[0] > 320 or snake_tail[0].current_position[0] < -320:
        #checks collision on x (first value in position tuple)
        screen.title("Snake hit wall, game over!")
        is_game_over = True
        # break
    if snake_tail[0].current_position[1] > 280 or snake_tail[0].current_position[1] < -280:
        #checks collision on y (second value in position tuple)
        # ChatGPT:  # The actual visible Y area is smaller because:
                    # the window title bar
                    # OS window borders
        # make the solution better
        screen.title("Snake hit wall, game over!")
        is_game_over = True
        # break
    if snake_tail[0].current_position == current_food.current_position:
        current_food.reset()
        new_tail = SnakePart()
        # new_tail = Turtle(shape="square")
        # new_tail.penup()
        # new_tail.color("white")
        # new_tail.previous_position = None
        new_tail.goto(snake_tail[-1].previous_position)
        # new_tail.current_position = None
        ## this is needed
        snake_tail.append(new_tail)
        # snake_tail[snake_length-1].current_position = snake_tail[snake_length-1].previous_position
        ## snake_length is computed before I append the new tail so it does not work
        ## len(snake_tail)-1 should work
        # snake_tail[len(snake_tail)-1].current_position = snake_tail[snake_length-1].previous_position
        # as it does
        # BETTER TO INDEX LAST ITEM IN LIST AS SNAKE_TAIL[-1] AS THIS ALWAYS RETURNS
        # LAST ITEM IN LIST AT THE CURRENT POINT IN CODE
        # like so
        snake_tail[-1].current_position = snake_tail[-1].previous_position
        current_food = spawn_food()
        screen.title(f"Snake length: {snake_length+1}")
    whole_snake_position = []
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

# for Unresolved attribute reference 'current_position' for class 'Turtle'
# ChatGPT suggests creating a subclass:
# class SnakeSegment(Turtle):
#     def __init__(self):
#         super().__init__(shape="square")
#         self.penup()
#         self.color("white")
#         self.current_position = (0, 0)
#         self.previous_position = (0, 0)
    #super() refers to the parent class (Turtle).
    # “Call the Turtle constructor with the shape square.”
    # Equivalent (but less clean):
    # Turtle.__init__(self, shape="square")
    # But using super() is better because:
    # It works with multiple inheritance
    # It’s cleaner and more Pythonic
    # It avoids hardcoding the parent class name