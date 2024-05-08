import busio
import board
import adafruit_amg88xx
import numpy as np
from PIL import Image, ImageTk

#i2c_bus = busio.I2C(board.SCL, board.SDA)
#amg = adafruit_amg88xx.AMG88XX(i2c_bus)

def obtener_imagen_termica():
    try:
        pixels = amg.pixels
        # Escala los valores de temperatura a un rango de 0-255
        pixels = (np.array(pixels) - np.min(pixels)) / (np.max(pixels) - np.min(pixels)) * 255
        pixels = np.uint8(pixels)
        # Convierte los píxeles en una imagen, redimensiona para mejor visualización
        imagen = Image.fromarray(pixels, 'L').resize((256, 256))
        return ImageTk.PhotoImage(imagen)
    except Exception as e:
        print("Error al obtener imagen térmica:", e)
        return None
