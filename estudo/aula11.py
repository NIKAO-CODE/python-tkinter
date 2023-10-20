#Usando matplotlib no tkinter
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


janela = Tk()
janela.title("Gráficos")
janela.geometry("470x250")

# Criando nova figura
figura = plt.Figure(figsize=(8, 4), dpi=60)
ax = figura.add_subplot(111)


canva = FigureCanvasTkAgg(figura, janela)
canva.get_tk_widget().grid(row=0, column=0)


# Fixing random state for reproducibility
np.random.seed(19680801)


# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')



janela.mainloop()
