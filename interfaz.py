# Código para realizar una interfaz donde se use una API para obtener datos de una ciudad y mostrarlos en pantalla.
# También se abrirá la visualizacion de una cámara termica que despliega la imagen en tamaño de 32x32 pixeles. (AMG8833)
# Por último mostrará un "led" para saber si se encendió el aspersor dependiendo de si la planta requiere de agua.

import tkinter as tk
from PIL import Image, ImageTk
from lib_clima import obtener_clima
from lib_cam_term import obtener_imagen_termica

def actualizar_interfaz(ciudad):
    clima = obtener_clima(ciudad)
    if clima:
        label_clima.config(text=f"{clima['ciudad']}: {clima['temperatura']}°C, Humedad: {clima['humedad']}%")
    else:
        label_clima.config(text="Datos no disponibles.")

def actualizar_imagen_termica():
    imagen_tk = obtener_imagen_termica()
    canvas.create_image(0, 0, anchor='nw', image=imagen_tk)
    canvas.image = imagen_tk  # Guardar referencia para evitar que se pierda
    root.after(500, actualizar_imagen_termica)  # Actualizar cada 500 ms

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Monitoreo y Riego")

# Etiqueta para la información del clima
label_clima = tk.Label(root, text="Cargando datos del clima...", font=('Arial', 16))
label_clima.pack(pady=20)

print("Cargando datos del clima...")

# Espacio para la imagen del sensor térmico
canvas = tk.Canvas(root, bg='black')
canvas.pack(pady=50)
# Modifica el tamaño del canvas para ajustarse a la imagen redimensionada
canvas.config(width=256, height=256)

# Iniciar la actualización de la imagen térmica
actualizar_imagen_termica()

print("Cargando imagen del sensor térmico...")

# LEDs para el sistema de riego
label_led_verde = tk.Label(root, text="Open", fg='green', font=('Arial', 24))
label_led_rojo = tk.Label(root, text="Closed", fg='red', font=('Arial', 24))
label_led_rojo.pack(side='left', padx=50)
label_led_verde.pack(side='right', padx=50)

print("Cargando estado del sistema de riego...")

# Iniciar la actualización de la interfaz
actualizar_interfaz("Monterrey")

print("Listo.")

root.mainloop()
