import random
from PIL import Image
from random import *

img = Image.open("./photos/file_0.jpg").convert('RGB')
width, height = img.size

def DarkFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r/3), int(g/3), int(b/3)]
    return tuple(result)


def BrightFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*3), int(g*3), int(b*3)]
    return tuple(result)

def RedFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*3), int(g*1), int(b*1)]
    return tuple(result)

def GreenFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*1), int(g*3), int(b*1)]
    return tuple(result)

def BlueFilter(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    for color in (r, g, b):
        result = [int(r*1), int(g*1), int(b*3)]
    return tuple(result)

def Drugs_eye(r: int, g: int, b: int) -> tuple[int, int, int]:
    result = []
    if r == 90 and g == 141 and b == 61:
        result = [int(randrange(25, 250)), int(randrange(25, 250)), int(randrange(25, 250))]
    elif r == 165 and g ==94 and b ==60:
        result = [int(250), int(20), int(5)]
    elif r ==74 and g ==114 and b == 52:
        result = [int(randrange(25, 250)), int(randrange(25, 250)), int(randrange(25, 250))]
    else:
        result = [r,g, b]
    return tuple(result)


def apply_filter(img: Image.Image, filt) -> Image.Image:
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = img.getpixel((i, j))
            new_pixel = filt(r,g,b)
            img.putpixel((i, j), new_pixel)
    img.save('./new_photos/new.jpg')
    return img
