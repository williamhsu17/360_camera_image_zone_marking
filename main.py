# -*- coding: utf-8 -*-
from PIL import Image

vfx_green_rgb = (0, 177, 64, 255)

marked_pixel = []

img = Image.open(r'image/main_hull.png')
img_width, img_height = img.size

for y in range(0, img_height):
    for x in range(0, img_width):
        if img.getpixel((x, y)) == vfx_green_rgb:
            marked_pixel.append((x,y))
