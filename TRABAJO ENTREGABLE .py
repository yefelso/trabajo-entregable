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
#------- Label y entry Apallido --------------------------------
obtenerApellido=StringVar()
lApellido = Label(miFrame, text='Apellido:')
lApellido.grid(row=1, column=0, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=1, column=1, pady=5, padx=5)