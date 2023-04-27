#interfaz

from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.title("interface calculadora")


mainFramearriba = ttk.Frame(raiz)#Frame para colocar el texto y la imagen de arriba
mainFramearriba.grid()

mainFramenums = ttk.Frame(raiz)
mainFramenums.grid()

ttk.Label(mainFramearriba, text="Calculadora basica").grid(column=0, row=0)

#mainFramearriba


#mainFramenums
#botones primera fila(columna)
ttk.Button(mainFramenums, text="AC",width=5).grid(column=0,row=0)
ttk.Button(mainFramenums, text="7",width=5).grid(column=0,row=1)
ttk.Button(mainFramenums, text="4",width=5).grid(column=0,row=2)
ttk.Button(mainFramenums, text="1",width=5).grid(column=0,row=3)
ttk.Button(mainFramenums, text="0",width=5).grid(column=0,row=4)

#botones segunda fila
ttk.Button(mainFramenums, text="8",width=5).grid(column=1,row=1)
ttk.Button(mainFramenums, text="5",width=5).grid(column=1,row=2)
ttk.Button(mainFramenums, text="2",width=5).grid(column=1,row=3)
ttk.Button(mainFramenums, text=".",width=5).grid(column=1,row=4)

#botones tercera fila
ttk.Button(mainFramenums, text="9",width=5).grid(column=2,row=1)
ttk.Button(mainFramenums, text="6",width=5).grid(column=2,row=2)
ttk.Button(mainFramenums, text="3",width=5).grid(column=2,row=3)
ttk.Button(mainFramenums, text="=",width=5).grid(column=2,row=4)

#botones operaciones
ttk.Button(mainFramenums, text="/",width=5).grid(column=3,row=1)
ttk.Button(mainFramenums, text="*",width=5).grid(column=3,row=2)
ttk.Button(mainFramenums, text="-",width=5).grid(column=3,row=3)
ttk.Button(mainFramenums, text="+",width=5).grid(column=3,row=4)

raiz.mainloop()