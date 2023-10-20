from tkinter import *

janela = Tk()

# usando gerenciador de geometria Pack
vermelho = Button(janela, text="vermelho", fg="red")
vermelho.pack(side=TOP)

verde = Button(janela, text="verde", fg="green")
verde.pack(side=RIGHT)

amarelo = Button(janela, text="amarelo", fg="yellow")
amarelo.pack(side=BOTTOM)

azul = Button(janela, text="azul", fg="blue")
azul.pack(side=LEFT)

janela.mainloop()