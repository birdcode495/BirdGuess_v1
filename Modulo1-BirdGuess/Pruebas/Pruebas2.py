from tkinter import *

import random


'''casa = [["fe", 12], ["erase", 23], ["rata", 15], ["gato", 18]]

c = random.randint(0, len(casa) - 1)

del casa[c]

d = float(casa[0][1])

del casa[2]

print(casa)

print(len(casa))'''

raiz = Tk()


cv = "Accipiter bicolor.png"

miFrame=Frame(raiz)

miFrame.pack()

miImagen=PhotoImage(file=cv)

Label(miFrame, image=miImagen).pack()








raiz.mainloop()

