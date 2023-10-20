from tkinter import *

janela = Tk()
janela.title("Label")
janela.geometry("300x200")

label = Label(janela, text="Primeiro botão")
label.grid(column=0, row=0)

def ola():
    print("Olá, mundo! Eu sou filho de Jesus Cristo")
    label.configure(text="Olá, mundo! Eu sou filho de Jesus Cristo")

button = Button(janela, text="Clique aqui", command=ola)
button.grid(column=1, row=0)


janela.mainloop()