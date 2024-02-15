#Crear botones
from tkinter import *

def sumar():
    r.set(str(float(n1.get()) + float(n2.get())))
    borrar()

def restar():
    r.set(str(float(n1.get()) - float(n2.get())))
    borrar()

def multiplicar():
    r.set(str(float(n1.get()) * float(n2.get())))
    borrar()

def dividir():
    r.set(str(float(n1.get()) / float(n2.get())))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd=15)

n1 = StringVar() #Variable para el primer número
n2 = StringVar() #Variable para el segundo número
r = StringVar() #Variable para el resultado

Label(root, text="Número 1").pack() #Empaquetar el texto
Entry(root, justify="center", textvariable=n1).pack() #Empaquetar el campo de texto
Label(root, text="Número 2").pack() #Empaquetar el texto
Entry(root, justify="center", textvariable=n2).pack() #Empaquetar el campo de texto

#Crear botones
Button(root, text="Sumar", command=sumar).pack()
Button(root, text="Restar", command=restar).pack()
Button(root, text="Multiplicar", command=multiplicar).pack()
Button(root, text="Dividir", command=dividir).pack()


Label(root, text="\nResultado").pack() #Empaquetar el texto
Entry(root, justify="center", textvariable=r, state="disabled").pack()



# Finalmente bucle de la aplicación
root.mainloop()