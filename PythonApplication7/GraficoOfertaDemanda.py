import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

def Chart():

    vDemanda = tbox_Demanda.get()
    vOferta = tbox_Oferta.get()

    vDemanda = vDemanda.split(',')
    vOferta = vOferta.split(',')

    print(vDemanda)
    print(vOferta)
    print('\n')

   # Ex. Demanda: 135,104,81,68,53,3; Ex. Oferta: 26,53,81,98,110,121; Ex. Preço: 4,5,6,7,8,9.
    d = {'Demanda': list(map(int,vDemanda)), 'Oferta': list(map(int,vOferta))}

    dataFrame = pd.DataFrame(data=d)
    dataFrame.index = [4,5,6,7,8,9] #preço
    print(dataFrame)

    dataFrame.plot()
    plt.plot(dataFrame, 's', color='black')
    plt.title("Equilíbrio de Preço")

    plt.grid(True)
    plt.xlabel("Preço")
    plt.ylabel("Quantidade")

    plt.show()

#
window = Tk()
window.title("Economia - Equilíbrio de Oferta e Demanda")

#Demanda
lb_Demanda = Label(window, text = 'Demanda:')
lb_Demanda.place(x=6,y=6)

tbox_Demanda = Entry(window)
tbox_Demanda.place(x=6, y=35)

#Oferta
lb_Oferta = Label(window, text = 'Oferta:')
lb_Oferta.place(x=6,y=70)

tbox_Oferta = Entry(window)
tbox_Oferta.place(x=6, y=99)


btn = Button(window, width=10, text='Gerar', command=Chart);
btn.place(x=6, y=150)

window.geometry("500x300+490+230") #largura x altura # pos. tela

window.mainloop()
#




