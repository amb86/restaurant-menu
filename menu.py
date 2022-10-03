import sqlite3
from tkinter import *

#config de la raiz
root = Tk()
root.title("Bar don Andrés - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   Bar don Andrés   ", fg="darkgreen", font=("Times New Roman", 28, "bold italic")).pack()
Label(root, text="Menú del día", fg="green", font=("Times New Roman", 28, "bold italic")).pack()
#separacion de titulos y categoría
Label(root, text="").pack

#conexion a bd
conexion = sqlite3.connect("restaurante02.db")
cursor = conexion.cursor()

#buscar las categorias y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1],fg="black", font=("Times New Roman", 20, "bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1],fg="gray", font=("Times New Roman", 15, "italic")).pack()

#Precio del menu
Label(root, text="12€ (IVA inc.)",fg="black", font=("Times New Roman", 12, "bold")).pack(side="right")


root.mainloop()
