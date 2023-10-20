# Criando uma ComboBox (Caixa de seleção)
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Criando ComboBox")
janela.geometry("300x300")


combo = Combobox(janela)
combo["values"] = (1, 2, "Nícolas", "Brasil")
combo.current(0)
combo.grid(column=0, row=0)


def obter(eventObject):
    value = combo.get()
    label = Label(janela, text=value)
    label.grid(column=0, row=1)

combo.bind("<<ComboboxSelected>>", obter)

janela.mainloop()