#Criando checkbutton
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("CheckButton")
janela.geometry("200x200")


def test():
    print("Valor do checkbutton : ", estado.get())

#StringVar(); BooleanVar()
estado = IntVar()


chek = Checkbutton(janela, text="escolha", var=estado, onvalue=1, offvalue=0, command=test)
chek.grid(column=0, row=0)

#inicia com o box marcado
estado.set(1)


janela.mainloop()