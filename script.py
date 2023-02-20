import browser
from browser import document, window

def make_greyscale():
    from PIL import Image
    img=Image.open('1.jpg')
    pixels=img.load()
    width,height=img.size
    output=Image.new('RGB',(width,height))
    pixels_out=output.load()
    for y in range(height):
        for x in range(width):
            avg_colors=tuple([sum([pixels[x,y][i] for i in range(3)])//3 for i in range(3)])
            pixels_out[x,y]=avg_colors
    output.save('1 copy.jpg')
