#Estudiar labels de tkinter
from tkinter import *   # Importa el módulo tkinter

root = Tk()             # Crea una ventana (padre)

#Configura el marco
frame = Frame(root, width=480, height=320) #creamos un frame con dimensiones (hijo)
frame.pack()

#Configura el label
label = Label(frame, text="Hola Mundo") #creamos un label con texto
#label.pack() #empaquetamos el label para que aparezca en el marco
#en lugar de pack puedo emplazarlo
label.place(x=100, y=100) #emplazamos el label en el marco

#Finalmente bucle de la aplicación
root.mainloop()         # Muestra la ventana