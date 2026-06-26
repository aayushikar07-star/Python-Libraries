import turtle
import colorsys
import math 

def draw_vortex():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Vortex Pattern")
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(10, 0)  # Disable automatic screen updates for smoother animation
    iterations = 360
    cycles = 6

    for i in range(iterations):
        hue = i / iterations
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)
        t.pensize(abs(math.sin(math.sin(i * 0.05))) * 2 + 1)  # Vary pen size based on sine wave
        angle = i * (360 /cycles) + (i * 0.5)  # Adjust angle for vortex effect
        distance = 16 * math.sqrt(i)  # Increase distance based on square root for spiral effect
        t.penup()
        t.goto(0,0)
        t.setheading(angle)
        t.forward(distance)
        t.pendown()
        t.begin_fill()
        t.fillcolor(colorsys.hsv_to_rgb((hue+0.5)% 1.0,0.8,0.3))

        for _ in range(3):  # Draw a triangle at each point
            t.forward(i*0.15)
            t.right(144)
            t.forward(i*0.15)
            t.left(72)
        t.end_fill()

    screen.update()
    turtle.done()


if __name__ == "__main__":
    draw_vortex()
