import random
import turtle as t
import colorgram
colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]


t.colormode(255)
alex = t.Turtle()
alex.speed("fastest")
alex.hideturtle()
num = 0
for _ in range(10):
    num += 1
    for dot in range(10):
        alex.dot(20, random.choice(color_list))
        alex.penup()
        alex.forward(50)
        print(num)
    alex.home()
    alex.setheading(90)
    alex.fd(50 * num)
    print(num)
    alex.setheading(0)

screen = t.Screen()
screen.exitonclick()
