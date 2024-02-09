# Comenzando con Tkinter para creación de interfaces gráficas
from tkinter import *   # Importa el módulo tkinter

root = Tk()             # Crea una ventana (padre)
root.title("Hola Mundo")       # Título de la ventana
root.iconbitmap('favicon.ico') # Icono de la ventana
# (1, 1) deja dimensionar ancho y largo
# (0, 0) no deja dimensionar ancho y largo
# (1, 0) deja dimensionar ancho y no largo
# (0, 1) no deja dimensionar ancho y deja largo
root.resizable(1, 1)    # Permite redimensionar la ventana

#creamos un frame
frame = Frame(root, width=480, height=320) #creamos un frame con dimensiones (hijo)
frame.pack(fill='both', expand=1) #expandir el frame a toda la ventana
frame.config(cursor="pirate") #cambiar el cursor
frame.config(bg="lightblue") #cambiar el color de fondo
frame.config(bd=25) #cambiar el tamaño del borde
frame.config(relief="sunken") #cambiar el tipo de borde



root.mainloop()         # Muestra la ventana