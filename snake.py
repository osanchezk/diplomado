"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import turtle

grid = turtle.Turtle()

title("Snake")
fontSize = 18

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 20, 'red')
        goto(0, -fontSize * 2)
        write("   GAME OVER    ",False, align="center",font=("Courier",fontSize,"bold"))
        bgcolor('white')
        #update()
        return

    snake.append(head)

    if head == food:
        #print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 20, 'blue')

    square(food.x, food.y, 20, 'green')
    #update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
grid = turtle.Turtle()
grid.speed(0)
grid.hideturtle()
grid.penup()
grid.goto(-240, 240)
grid.direction = "right"
grid.pendown()
grid.forward(480)
grid.right(90)
grid.forward(480)
grid.right(90)
grid.forward(480)
grid.right(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.left(180)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
grid.right(90)
grid.forward(20)
grid.right(90)
grid.forward(480)
grid.left(90)
grid.forward(20)
grid.left(90)
grid.forward(480)
tracer(False)
bgcolor('white')
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
