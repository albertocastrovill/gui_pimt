from Adafruit_AMG88xx import Adafruit_AMG88xx
import numpy as np
from scipy.interpolate import griddata
from PIL import Image, ImageTk
from colour import Color

def obtener_imagen_termica():
    sensor = Adafruit_AMG88xx()
    MINTEMP = 26
    MAXTEMP = 32
    COLORDEPTH = 1024
    
    blue = Color("indigo")
    colors = list(blue.range_to(Color("red"), COLORDEPTH))
    colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]
    
    points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
    grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]
    
    pixels = sensor.readPixels()
    pixels = [map_pixel(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
    
    image = Image.new("RGB", (32, 32))
    for ix, row in enumerate(bicubic):
        for jx, pixel in enumerate(row):
            color = colors[constrain(int(pixel), 0, COLORDEPTH - 1)]
            image.putpixel((jx, ix), color)
    
    return ImageTk.PhotoImage(image.resize((256, 256), Image.NEAREST))

def map_pixel(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))