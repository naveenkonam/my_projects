import turtle

def draw_rhombus(some_class):
    for i in range(1,5):
        some_class.forward(100)
        some_class.right(90)

window = turtle.Screen()
window.bgcolor("blue")
brad= turtle.Turtle()
brad.speed(1)

for j in range(1,100):
    draw_rhombus(brad)
    brad.right(10)

window.exitonclick()
