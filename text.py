#Crear textos largos
from tkinter import *

root = Tk()

#Crear campo de texto
texto = Text(root)
texto.pack() #Empaquetar el campo de texto
# Configurar el campo de texto
# padx y pady son los margenes internos
texto.config(width=30, height=10, font=("Consolas", 12), padx=15, pady=15,\
              selectbackground="red")


# Finalmente bucle de la aplicación
root.mainloop()