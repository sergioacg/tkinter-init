#Crear botones
from tkinter import *

def crear_label():
    label = Label(root, text="Label creado con un botón")
    label.pack()

root = Tk()

#Crear botones
#Button(root, text="Clickeame", command=lambda: print("Me clickeaste")).pack()
Button(root, text="Clickeame", command=crear_label).pack()

# Finalmente bucle de la aplicación
root.mainloop()