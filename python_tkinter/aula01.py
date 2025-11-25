from tkinter import *

# widgets = Elementos da interface gráfica: botões, caixas de texto, rótulos e imagens.
# windows = Serve como um recipiente para armazenar ou conter esses widgets.

window = Tk() # Instancia uma instância de uma janela.
window.geometry("420x420")
window.title("Meu primeiro Tkinter")

icon = PhotoImage(file="images/logo.png")
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop() # Coloca a janela na tela do computador, escute os eventos.
