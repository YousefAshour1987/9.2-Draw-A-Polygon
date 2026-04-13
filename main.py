from turtle import *

screen = Screen()
screen.title("polygons")
screen.bgcolor("teal")
screen.setup(width = 800, height = 600)


def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(200/sides)
        turtle.left(360/sides)
    turtle.end_fill()


quad = {3: "triangle", 
        4: "quadrilateral", 
        5: "pentagon", 
        6: "Hexagon",
        7: "Septagon",
        8: "Octagon",
        9: "Unknown"

}
pen = Turtle()
pen.shape("turtle")
pen.color("white")
pen.speed(1)

pen2 =Turtle()
pen.ht()
pen2.pu()
pen2.goto(0,-100)
pen2.pd()
pen2.color("white")

while True:
    sides = int(input("Enter number of polygon sides: "))
    pen.clear()
    if sides < 3:
        pen.write("polygons must have at least 3 sides.")
    elif sides !=4:
        regular_polygon(pen, sides)
        pen2.write(quad[sides])
    else:
        answer = int(input("How many pairs of parallel sides? "))
        if answer == 0:
            pen.begin_fill()
            pen2.write("Unknown quadrilateral")
            pen.goto(0, 0)
            pen.goto(175, 85)
            pen.goto(47, -23)
            pen.goto(-100, 0)
            pen.goto(0, 0)
            pen.end_fill()
        elif answer == 1:
            pen.begin_fill()
            pen2.write("This is a trapezoid")
            pen.goto(-100, 0)
            pen.forward(100)
            pen.left(135)
            pen.forward(100)
            pen.setheading(180)
            pen.forward(50)
            pen.goto(-175,0)
            pen.end_fill()
        elif answer == 2:
            check = input(
"Does this have all 4 interior angles of 90 degrees? Yes/No: "
)
            if check == "No":
                for i in range(2):
                    pen.begin_fill()
                    pen2.write("This is a parallelogram")
                    pen.forward(120)
                    pen.left(60)
                    pen.forward(120)
                    pen.left(180-60)
                    pen.end_fill()
            elif check == "Yes":
                length = input("Are all 4 sides the same length? Yes/No: ")
                if length == "No":
                    for i in range(2):
                        pen.begin_fill()
                        pen2.write("This is a rectangle")
                        pen.forward(100)
                        pen.left(90)
                        pen.forward(200)
                        pen.left(180-90)
                        pen.end_fill()
                elif length == "Yes":
                    pen.begin_fill()
                    pen2.write("This is a square")
                    for i in range(4):
                        
                        pen.forward(100)
                        pen.left(90)
                    pen.end_fill()
                   
screen.exitonclick()