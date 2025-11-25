from tkinter import *

def submit():
    print(f"The temperature is {scale.get()}°C.")

window = Tk()

hotImage = PhotoImage(file="images/fire.png")
hotImage = hotImage.subsample(10, 10)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(
    window,
    from_=100,
    to=0,
    length=600,
    orient=VERTICAL, # escala de orientação.
    font=("Consolas", 20),
    tickinterval=10, # adiciona um indicador numeral para o valor.
    # showvalue=0, # oculta o valor atual.
    resolution=5, # incrementa um valor no "scroll".
    troughcolor="#69EAFF",
    fg="#FF1C00",
    bg="#111111"
    )
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"]) # é onde vai iniciar.
scale.pack()

coldImage = PhotoImage(file="images/ice.png")
coldImage = coldImage.subsample(10, 10)
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(
    window,
    text="submit",
    command=submit
    )
button.pack()

window.mainloop()
