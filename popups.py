#Crear popups
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()
root.title("Popups")
root.config(bd=15)

def test():
    #MessageBox.showinfo("Hola", "Hola mundo")
    #MessageBox.showwarning("Alerta", "Seccion solo para administradores")
    #MessageBox.showerror("Error", "Ha ocurrido un error inesperado")
    #resultado = MessageBox.askquestion("Salir", "¿Estas seguro que quieres salir sin guardar?")
    #if resultado == "yes":
    #    root.destroy()
    #resultado = MessageBox.askokcancel("Salir", "¿Estas seguro que quieres salir sin guardar?")
    #resultado = MessageBox.askyesno("Salir", "¿Estas seguro que quieres salir sin guardar?")
    #if resultado:
    #    root.destroy()
    #resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    #if resultado:
    #    root.destroy()

    #color = ColorChooser.askcolor(title="Elige un color")
    #print(color)

    #ruta = FileDialog.askopenfilename(title="Abrir un archivo",
    #                                  filetypes=(("Archivos de Excel", "*.xlsx"),))
    #print(ruta) #Devuelve la ruta del archivo seleccionado

    archivo = FileDialog.asksaveasfile(title="Guardar un archivo",
                                    mode="w",
                                    defaultextension=".txt")
    print(archivo) 
    if archivo is not None:
        archivo.write("Hola")
        archivo.close()



Button(root, text="Pulsar para ver el mensaje", command=test).pack()



root.mainloop()