# Comenzando con Tkinter para creación de interfaces gráficas
from tkinter import *   # Importa el módulo tkinter

root = Tk()             # Crea una ventana
root.title("Hola Mundo")       # Título de la ventana
root.iconbitmap('favicon.ico') # Icono de la ventana
# (1, 1) deja dimensionar ancho y largo
# (0, 0) no deja dimensionar ancho y largo
# (1, 0) deja dimensionar ancho y no largo
# (0, 1) no deja dimensionar ancho y deja largo
root.resizable(1, 1)    # Permite redimensionar la ventana
root.mainloop()         # Muestra la ventana