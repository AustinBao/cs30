import turtle

import math

def find_diagonal_coordinate(x1, y1, distance, leg):
    # Assuming the diagonal makes a 45-degree angle with the x-axis
    if leg == "l":
        angle = math.radians(315)
    else:
        angle = math.radians()
    # Calculate the change in x and y based on the distance and angle
    delta_x = distance * math.cos(angle)
    delta_y = distance * math.sin(angle)

    # Calculate the ending coordinates
    x2 = x1 + delta_x
    y2 = y1 + delta_y

    return x2, y2

    
# 🤫🧏‍♂️

def drawStickman(x, y, r, body, rightArm, leftArm, rightLeg, leftLeg):
    turtle.title("Stickman")
    t = turtle.Turtle()
    
    t.penup()
    t.pensize(3)
    t.goto(x, y)
    t.pendown()

    # Draw head
    t.circle(r)
    t.right(90)
    t.forward(body/2)
    t.left(90)
    t.forward(rightArm)
    t.right(180)
    t.forward(rightArm + leftArm)
    t.left(180)
    t.forward(leftArm)
    t.right(90)
    t.forward(body/2)
    x1, y1 = t.pos()
    
    # x2, y2 = find_diagonal_coordinate(x1, y1, leftLeg)
    # print(x2,y2)
    # print(rightLeg)
    # t.goto(x2*-1, y2)
    # t.goto(x1, y1)
    # t.goto(x2, y2)




drawStickman(0, 0, 10, 20, 30, 10, 10, 10)
drawStickman(50, 0, 30, 40, 30, 10, 10, 10)

turtle.mainloop()  # or turtle.exitonclick()
