import colorsys
import math

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

rgb1 = (252, 249, 242)
hex = "#fcf9f2"

rgb2 = hex_to_rgb(hex)

distance = math.sqrt((rgb1[0] - rgb2[0])**2 + (rgb1[1] - rgb2[1])**2 + (rgb1[2] - rgb2[2])**2)
print(distance)
