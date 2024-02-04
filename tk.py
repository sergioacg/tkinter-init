# Comenzando con Tkinter para creación de interfaces gráficas
from tkinter import *   # Importa el módulo tkinter

root = Tk()             # Crea una ventana
root.title("Hola Mundo")       # Título de la ventana
root.iconbitmap('favicon.ico') # Icono de la ventana
root.resizable(1, 1)    # Permite redimensionar la ventana
root.mainloop()         # Muestra la ventana