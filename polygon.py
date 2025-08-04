import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(width=800, height=600)
polygon= turtle.Turtle()

num_sides = 6
angle = 360 / num_sides

for _ in range(num_sides):
    polygon.forward(100)
    polygon.right(angle)
turtle.done()