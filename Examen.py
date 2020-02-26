import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import Menu

ventana = tk.Tk()
ventana.title ("EDUCACIÓN FÍSICA")

#PREGUNTA 1
label = ttk.Label (ventana, text = "1) Ecriba cual es su deporte favorito. Justifique su respuesta").grid(column=1, row=4)
scroll_ancho=15
scroll_alto=2
caja1 = scrolledtext.ScrolledText(ventana, width = scroll_ancho, height = scroll_alto, wrap=tk.WORD)
caja1.grid(column=1, row = 5)

#PREGUNTA 2
label = ttk.Label (ventana, text = "2) Explique en que consiste el pivote en BasquetBall").grid(column=1, row=6)
scroll_ancho=15
scroll_alto=2
caja2 = scrolledtext.ScrolledText(ventana, width = scroll_ancho, height = scroll_alto, wrap=tk.WORD)
caja2.grid(column=1, row = 7)

#PREGUNTA 3
def est():

    selector = opcion.get()

label2= ttk.Label (ventana, text=" 3) Deporte que se juega en equipo de 6  a 11").grid (column=1, row=8)

opcion = tk.StringVar()
radio1 = tk.Radiobutton (ventana, text= "Golf", variable =opcion, value="Casado", command = est)
radio1.grid (column = 1,row = 9, sticky = tk.W)
radio1.select()

radio2 = tk.Radiobutton (ventana, text= "Futbol", variable =opcion, value="Soltero", command = est)
radio2.grid (column = 2,row = 9, sticky = tk.W)

radio3 = tk.Radiobutton (ventana, text= "Voleyball", variable =opcion, value="viudo", command = est)
radio3.grid (column = 3,row = 9, sticky = tk.W)

#PREGUNTA 4
def est1():

    selector1 = opcion.get()

label3= ttk.Label (ventana, text=" 4) Seleccione lo que se debe hacer antes de practicar algun deporte.").grid (column=1, row=10)

opcion = tk.StringVar()
radio1 = tk.Radiobutton (ventana, text= "Comer", variable =opcion, value="Casado", command = est1)
radio1.grid (column = 1,row = 11, sticky = tk.W)
radio1.select()

radio2 = tk.Radiobutton (ventana, text= "Cantar", variable =opcion, value="Soltero", command = est1)
radio2.grid (column = 2,row = 11, sticky = tk.W)

radio3 = tk.Radiobutton (ventana, text= "Calentar", variable =opcion, value="viudo", command = est1)
radio3.grid (column = 3,row = 11, sticky = tk.W)

#PREGUNTA 5

#CALIFICAR
def cal():
    mBox.showinfo("Examen Aprobado")

boton = ttk.Button (ventana, text="CALIFICAR", command = cal)
boton.grid(column=5, row=15)


ventana.mainloop()