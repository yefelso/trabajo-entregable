from tkinter import *
 
root = Tk()
root.title('FERRETERIA EL TORNILLO FELIZ')
 
miFrame = Frame(root)
miFrame.pack()
#------- Label y entry DNI --------------------------------
obtenerDni=StringVar()
lDni = Label(miFrame, text='DNI:')
lDni.grid(row=0, column=0, sticky='e', pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=0, column=1, pady=5, padx=5)
