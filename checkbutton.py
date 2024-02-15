#Crear checkbutton
from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    if(azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"
    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar() # 1 si, 0 no
azucar = IntVar() # 1 si, 0 no

imagen = PhotoImage(file="cafe.gif")
#redicir el tamaño de la imagen
imagen = imagen.subsample(2) #Divide la imagen entre 2

Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="right")

Label(frame, text="¿Como quieres el cafe?").pack( anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, \
            command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, \
            command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()


#Bucle de la aplicacion
root,mainloop()