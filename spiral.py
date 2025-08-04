import turtle
board = turtle.Screen()
board.bgcolor("lightblue")
board.title("turtle drawing")
board.setup(width=800, height=600)
size = 8
t = turtle.Turtle()
for _ in range(50):  # Draw 50 squares in spiral
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
    size = size + 5  # Increase size for spiral effect
turtle.done()
