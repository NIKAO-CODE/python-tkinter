from tkinter import *

janela = Tk()
janela.geometry("200x200")

# usando gerenciador de geometria Grid
vermelho = Button(janela, text="vermelho", fg="red", width=7)
vermelho.grid(column=0, row=0)

verde = Button(janela, text="verde", fg="green", width=7)
verde.grid(column=1, row=0)

azul = Button(janela, text="azul", fg="blue", width=7)
azul.grid(column=1, row=1)

amarelo = Button(janela, text="amarelo", fg="yellow", width=7)
amarelo.grid(column=2, row=1)


janela.mainloop()