from tkinter import *

# button = você clica nele, e aí acontece alguma coisa.

count = 0

def click():
    global count
    count+=1
    print(f"Você clicou pela {count}º vez.")

window = Tk()

photo = PhotoImage(file="images/like.png")

button = Button(
    window,
    text="Clique-me!",
    command=click,
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    state=ACTIVE,
    image=photo,
    compound="bottom"
    )
button.pack()

window.mainloop()
