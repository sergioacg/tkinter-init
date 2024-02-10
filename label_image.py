#Estudiar labels de tkinter
from tkinter import *   # Importa el módulo tkinter

#Configura la raíz
root = Tk()             # Crea una ventana (padre)

imagen = PhotoImage(file="cafe.gif") # Crea un objeto PhotoImage
Label(root, image=imagen, bd=  0).pack()      # Muestra la imagen en la ventana (padre) con un borde de 0

#Finalmente bucle de la aplicación
root.mainloop()         # Muestra la ventana