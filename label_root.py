#Estudiar labels de tkinter
from tkinter import *   # Importa el módulo tkinter

#Configura la raíz
root = Tk()             # Crea una ventana (padre)

# Variables dinamicas StringVar
texto = StringVar() #creamos una variable dinamica de tipo string
texto.set("Un nuevo texto") #asignamos un valor a la variable dinamica

label = [0, 0, 0]
#Configura el label (forma 1)
#Label(root, text="Hola Mundo").pack(anchor= "nw") #creamos un label con texto y lo empaquetamos para que aparezca en la ventana
#Label(root, text="Otra etiqueta").pack(anchor= "center") 
#Label(root, text="Ultima etiqueta").pack(anchor= "se") 

#Configura el label (forma 2)
label[0] = Label(root, text="Hola Mundo") #creamos un label con texto
label[0].pack(anchor= "nw") #emplazamos el label en la ventana
label[1] = Label(root, text="Otra etiqueta") #creamos un label con texto
label[1].pack(anchor= "center") #emplazamos el label en la ventana
label[2] = Label(root, text="Ultima etiqueta") #creamos un label con texto
label[2].pack(anchor= "se") #emplazamos el label en la ventana

#bg = background, fg = foreground, font = tipo de letra
label[0].config(bg="green", fg="blue", font=("Verdana", 24)) #cambiamos el color de fondo, el color de la letra y el tipo de letra
label[0].config(textvariable=texto) #asignamos la variable dinamica al label


#Finalmente bucle de la aplicación
root.mainloop()         # Muestra la ventana