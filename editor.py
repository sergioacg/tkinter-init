from tkinter import *
from tkinter import filedialog

#Variable global para almacenar la ruta del archivo global
ruta = ""


def new():
    global ruta
    mensaje.set("New file")
    text.delete(1.0, "end") #Borrar desde el caracter 1 hasta el final
    root.title(ruta + " - Text Editor")


def open_file():
    global ruta
    mensaje.set("Open file")
    ruta = filedialog.askopenfilename(initialdir=".", filetypes=(("Text files", "*.txt"),), 
                                      title="Open file")
    if ruta != "":
        fichero = open(ruta,'r')
        contenido = fichero.read()
        text.delete(1.0, "end")
        text.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Text Editor")

def save():
    global ruta
    mensaje.set("Save file")
    if ruta != "":
        contenido = text.get(1.0, "end-1c")#Coger el contenido del texto desde el caracter 1 hasta el final menos el salto de linea
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File saved successfully")
    else:
        saveas()

def saveas(): 
    global ruta   
    mensaje.set("Save file as...")
    fichero = filedialog.asksaveasfile(title="Save file", mode="w", 
                                       defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = text.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File saved successfully")


# Crear el objeto Tk
root = Tk()

root.title("Editor de texto")

#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0) #tearoff=0 para que no se pueda despegar
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...",    command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#Caja de texto central
text = Text(root)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

#Crear un monitor inferior en una label
mensaje = StringVar()
mensaje.set("Welcome to your Text Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)

root.mainloop()