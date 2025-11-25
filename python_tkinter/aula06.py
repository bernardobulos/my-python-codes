from tkinter import *

# radio button (botões de opção) = semelhante a um chebox, mas você só pode selecionar uma opção de um grupo.

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered a pizza!")
    elif(x.get() == 1):
        print("You ordered a hamburger!")
    elif(x.get() == 2):
        print("You ordered a hotdog!")
    else:
        print("Huh?")

window = Tk()

pizzaImage = PhotoImage(file="images/pizza.png")
pizzaImage = pizzaImage.subsample(13, 13)

hamburgerImage = PhotoImage(file="images/hamburger.png")
hamburgerImage = hamburgerImage.subsample(4, 4)

hotdogImage = PhotoImage(file="images/hotdog.png")
hotdogImage = hotdogImage.subsample(4, 4)

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index], # adiciona um texto nos radio buttons.
        variable=x, # agrupa os radio buttons se eles compartilharem a mesma variável.
        value=index, # atribui um valor diferente a cada radio button.
        padx=25, # adiciona espaçamento no eixo x.
        font=("Impact", 50),
        image=foodImages[index], # adiciona imagens nos radio buttons.
        compound="left", # adiciona imagens e texto (à esquerda) nos radio buttons.
        indicatoron=0, # elimina indicadores circulares.
        width= 375, # define a largura dos radio buttons.
        command=order # define um comando do radio buttons para a função 'order'.
    )
    radiobutton.pack(anchor=W)

window.mainloop()
