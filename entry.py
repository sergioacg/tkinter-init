from tkinter import *   # Importa el módulo tkinter

#Configura la raíz
root = Tk()             # Crea una ventana (padre)

frame = Frame(root, width=500, height=400) # Crea un objeto Frame
frame.pack()            # Muestra el objeto Frame en la ventana (padre)
# Crea un objeto Entry (caja de texto) con la raíz como padre
entry = Entry(frame)     # Crea un objeto Entry
entry.pack(side="right")            # Muestra el objeto Entry en la ventana (padre)

# crear label
label = Label(frame, text="Nombre")
label.pack(side="left")           # Muestra el objeto Label en la ventana (padre)

frame2 = Frame(root, width=500, height=400) # Crea un objeto Frame
frame2.pack()            # Muestra el objeto Frame en la ventana (padre)
# Crea un objeto Entry (caja de texto) con la raíz como padre
entry2 = Entry(frame2)     # Crea un objeto Entry
entry2.pack(side="right")            # Muestra el objeto Entry en la ventana (padre)

# crear label
label2 = Label(frame2, text="Apellido")
label2.pack(side="left")           # Muestra el objeto Label en la ventana (padre)


#FINALMENTE BUCLE DE LA APLICACIÓN
root.mainloop()         # Muestra la ventana