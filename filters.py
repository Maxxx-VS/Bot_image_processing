from PIL import Image

img = Image.open("C:/Users/hot-z/pythonProject_Bot/photos/file_0.jpeg").convert('RGB')
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

def apply_filter(img: Image.Image, DarkFilter) -> Image.Image:
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = img.getpixel((i, j))
            new_pixel = DarkFilter(r,g,b)
            img.putpixel((i, j), new_pixel)
    img.save("C:/Users/hot-z/pythonProject_Bot/photos/file_0_NEW.jpeg")
    return img
