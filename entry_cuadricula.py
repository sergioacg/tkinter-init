#Haremos una cuadricula para no tener que usar rootS

from tkinter import *   # Importa el módulo tkinter

#Configura la raíz
root = Tk()             # Crea una ventana (padre)

# crear label
label = Label(root, text="Nombre de nacimiento porfavor:")
#row = fila, column = columna, sticky = alineacion, padx = pixeles de separacion en x, 
#pady = pixeles de separacion en y
label.grid(row=0, column=0, sticky='e', padx=5, pady=5)           # Muestra el objeto Label en la ventana (padre)
# Crea un objeto Entry (caja de texto) con la raíz como padre
entry = Entry(root)     # Crea un objeto Entry
entry.grid(row=0, column=1, padx=5, pady=5)           # Muestra el objeto Entry en la ventana (padre)

# crear label
label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky='e', padx=5, pady=5)
# Crea un objeto Entry (caja de texto) con la raíz como padre
entry2 = Entry(root)     # Crea un objeto Entry
entry2.grid(row=1, column=1, padx=5, pady=5)           # Muestra el objeto Entry en la ventana (padre)
entry2.config(show="*") #Para que la contraseña no se vea

#FINALMENTE BUCLE DE LA APLICACIÓN
root.mainloop()         # Muestra la ventana