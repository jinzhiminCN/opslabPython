#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

"""将图像转换为字符形式的图像"""
import os
from PIL import Image,ImageFont,ImageDraw
from src import App

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    image_file = App.resource_file("/opencv/green-spiral.jpg")
    im = Image.open(image_file)
    pix = im.load()

    ims = Image.new("RGB", (im.width,im.height), (255, 255, 255))
    dr = ImageDraw.Draw(ims)
    font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 10)

    txt = ""
    for i in range(im.height):
        for j in range(im.width):
            char = get_char(*im.getpixel((j,i)))
            txt += char
            dr.text((j,i),char, pix[j, i], font)
        txt += '\n'
    with open("output.txt", 'w') as f:
        f.write(txt)
    ims.save("tt.png")





