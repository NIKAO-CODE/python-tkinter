#Criando ListBox
from tkinter import *

janela = Tk()
janela.title("ListBox")
janela.geometry("250x200")

def test():
    l = Label(janela, text=listbox.get(ACTIVE), width=20)
    l.grid(column=1, row=0)


def test2():
    #(0, END) apaga tudo da lista
    listbox.delete(ANCHOR)


listbox = Listbox(janela, height=8)
listbox.grid(column=0, row=0)


listbox.insert(0, "PHP")
listbox.insert(1, "Python")
listbox.insert(2, "MySQL")
listbox.insert(END, "GCP")


lista = ["JavaScript", "Java", "C++"]

for i in lista:
    listbox.insert(END, i)

btn = Button(janela, text="Imprimir", command=test)
btn.grid(column=0, row=1)


btn_delete = Button(janela, text="Deletar", command=test2)
btn_delete.grid(column=0, row=2)


janela.mainloop()
