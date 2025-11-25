from tkinter import *

# label = Um widget de área que contém texto e/ou uma imagem dentro de uma janela.

window = Tk()

photo = PhotoImage(file="images/programmer.png")

label = Label(
    window,
    text="Hello, world!",
    font=("Arial", 40, "bold"),
    fg="#4e7bd4",
    bg="black",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="bottom"
    )

label.pack()
# label.place(x=0, y=0)

window.mainloop()
