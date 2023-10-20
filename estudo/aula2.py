from tkinter import *

janela = Tk()

# usando gerenciador de geometria Place
a = Button(janela, text="Usando place")
a.place(x=100, y=100)

b = Button(janela, text="Usando place")
b.place(x=50, y=50)

janela.mainloop()