#Criando RadioButton
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("RadioButton")
janela.geometry("200x200")


def obter():
    print("O valor do botão selecionado é: ", selecionado.get())


#StringVar(); BooleanVar()
selecionado = IntVar()


rad_1 = Radiobutton(janela, text="Primeiro", value=1, var=selecionado, command=obter)
rad_1.grid(column=0, row=0)

rad_1 = Radiobutton(janela, text="Segundo", value=2, var=selecionado, command=obter)
rad_1.grid(column=1, row=0)

rad_1 = Radiobutton(janela, text="Terceiro", value=3, var=selecionado, command=obter)
rad_1.grid(column=2, row=0)

#inicia com o radio marcado
selecionado.set(1)


janela.mainloop()
