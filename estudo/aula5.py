# entrada de dados com TKinter
from tkinter import *

janela = Tk()
janela.title("Criando uma Entry")
janela.geometry("300x300")

label_nome = Label(janela, text="Nome")
label_nome.grid(column=0, row=0)
nome = Entry(janela, width=20, state="disable")
nome.grid(column=1, row=0)

label_idade = Label(janela, text="Idade")
label_idade.grid(column=0, row=1)
idade = Entry(janela, width=20)
idade.grid(column=1, row=1)

label_pais = Label(janela, text="Pais")
label_pais.grid(column=0, row=2)
pais = Entry(janela, width=20)
pais.grid(column=1, row=2)


def testando():
    n = nome.get()
    i = idade.get()
    p = pais.get()

    label = Label(janela, text= n + " " + i + " " + p)
    label.grid(column=1, row=4)
    print(n, i, p)


b = Button(janela, text="Teste", bg="green", command=testando)
b.grid(column=0, row=4)



janela.mainloop()