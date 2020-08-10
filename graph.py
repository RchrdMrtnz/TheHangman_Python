import tkinter
from title import title
ventana = tkinter.Tk()
ventana.geometry("700x500")

etiqueta = tkinter.Label(ventana, text="The_Hangman")
etiqueta.pack()


etiqueta = tkinter.Label(ventana, text="© rchrd_mtnz", bg="grey")
etiqueta.pack(side=tkinter.BOTTOM, fill=tkinter.X)

cajadetexto = tkinter.Entry(ventana)
cajadetexto.pack()

pantalla = tkinter.Label(ventana)
pantalla.pack()

def input():
    texto=cajadetexto.get()
    pantalla["text"]=texto

boton1 = tkinter.Button(ventana, text="Click here or die",
                        command=input)
boton1.pack()

boton1 = tkinter.Button(ventana, text="Click here or live",
                        command=title)
boton1.pack()

ventana.mainloop()
