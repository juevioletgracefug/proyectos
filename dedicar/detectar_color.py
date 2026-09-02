import os
import tkinter as tk

root = tk.Tk()
root.withdraw()  # oculta la ventana, no la necesitamos visible

# Construye la ruta a rosa.png basada en dónde está este script, no en dónde lo ejecutas
ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rosa.png")

img = tk.PhotoImage(file=ruta_imagen)
r, g, b = img.get(0, 0)  # color del pixel en la esquina superior izquierda
print(f"Color de fondo detectado: #{r:02x}{g:02x}{b:02x}")