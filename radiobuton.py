# Radio buttons

from tkinter import *

def seleccionar():
    monitor.config(text=f"{opcion.get()}")

def reset():
    opcion.set(None)
    monitor.config(text="")

ventana = Tk()

#Un radio button siemopre tiene un valor por defecto que formarian en conjunto una posible opcion
opcion = IntVar() #Variable para el radio button

Radiobutton(ventana, text="Opción 1", value=1, variable=opcion, command=seleccionar).pack()
Radiobutton(ventana, text="Opción 2", value=2, variable=opcion, command=seleccionar).pack()
Radiobutton(ventana, text="Opción 3", value=3, variable=opcion, command=seleccionar).pack()

#Label monitor
monitor = Label(ventana)
monitor.pack()

#Boton reiniciar
Button(ventana, text="Reiniciar", command=reset).pack()


# Finalmente bucle de la aplicación
ventana.mainloop()