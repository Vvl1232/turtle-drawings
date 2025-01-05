from turtle import Turtle, Screen
import random as rd


#===================================hirst painting================================================

t = Turtle()
s = Screen()
s.colormode(255)
color_list = [
    (229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50),
    (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34),
    (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48),
    (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181),
    (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59),
    (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)
]

def hirst_paint():
    for _ in range(10):
        t.dot(20, rd.choice(color_list))
        t.forward(40)

def next_line():
    for _ in range(10):
        t.dot(20, rd.choice(color_list))
        t.forward(40)

def right():
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)

def left():
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

def draw_hirst_painting(rows):
    for _ in range(rows):
        hirst_paint()
        left()
        hirst_paint()
        right()
    
t.speed(0)
t.hideturtle()
t.penup()
t.backward(200)
draw_hirst_painting(3)
s.exitonclick()




#===================================dash line================================================
# t.penup()
# t.hideturtle()
# t.backward(150)
# t.pendown()
# t.color(rd.choice(color_list))
# t.pensize(4)
# def dash():
#     for _ in range(20):
#         t.forward(10)
#         t.up()              # penup()/pu()/up()
#         t.forward(10)
#         t.down()            # pendown()/pd()/down()
# dash()

# s.exitonclick()









# #===================================circle================================================
# t.hideturtle()
# t.penup()
# t.backward(50)
# t.pendown()
# t.pensize(7)
# def circle():
#     t.color(120, 180, 180)
#     t.circle(100)
# circle()
# s.exitonclick()


















# #===================================shape overlapping pattern================================================
# t.hideturtle()
# t.penup()
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(180)
# t.pendown()
# t.pensize(6)
# def triangle():
#     for _ in range(3):
#         t.forward(100)
#         t.right(120)
# triangle()

# def square():
#     for _ in range(4):
#         t.forward(100)
#         t.right(90)
#         t.color('red')
# square()

# def penta():
#     for _ in range(5):
#         t.forward(100)
#         t.right(72)
#         t.color('green')
# penta()

# def hexa():
#     for _ in range(6):
#         t.forward(100)
#         t.right(60)
#         t.color('purple')
# hexa()

# def hepta():
#     for _ in range(7):
#         t.forward(100)
#         t.right(51.43)
#         t.color('orange')
# hepta()

# def octa():
#     for _ in range(8):
#         t.forward(100)
#         t.right(45)
#         t.color("black")
# octa()

# def nona():
#     for _ in range(9):
#         t.forward(100)
#         t.right(40)
#         t.color('lightseagreen')
# nona()

# def deca():
#     for _ in range(10):
#         t.forward(100)
#         t.right(36)
#         t.color('blue')
# deca()

# s.exitonclick()












# #===================================random design of turtle random walk================================================
# def random_walk():
#     for _ in range(100):
#         angle = rd.choice([90, 45, 270,135,180,225,315])  #it chooses angle randomly from the list
#         t.color(rd.random(), rd.random(), rd.random())      #it sets color value randomly with respect to RGB value
#         t.setheading(angle)
#         t.forward(30)

# t.hideturtle()
# t.speed(0)  
# t.pensize(20)  
# random_walk()
# s.exitonclick()













# #===================================spirograph================================================

# def spirograph():
#     for _ in range(100):
#         t.color(rd.random(), rd.random(), rd.random())
#         t.circle(100)
#         t.right(5)

# t.hideturtle()
# t.speed(0)  
# t.pensize(4)  
# spirograph()


# s.exitonclick()