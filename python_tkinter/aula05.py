from tkinter import *

def display():
    if (x.get() == 1): # Você pode usar "boolean" (True) e "string" ("YES") também se desejar.
        print("You agree! 😀")
    else:
        print("You don't agree... 😔")

window = Tk()

x = IntVar() # Você pode usar "BooleanVar" (True) e "StringVar" ("YES") também se desejar.

python_photo = PhotoImage(file="images/logo.png")
python_photo = python_photo.subsample(7, 7) # Reduz a imagem dividindo seu tamanho por esses valores.

check_button = Checkbutton(
    window,
    text="I agree to something",
    variable=x,
    onvalue=1, # Você pode usar "boolean" (True) e "string" ("YES") também se desejar.
    offvalue=0, # Você pode usar "boolean" (False) e "string" ("NO") também se desejar.
    command=display,
    font=("Arial", 20),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    padx=25,
    pady=10,
    image=python_photo,
    compound="left"
    )
check_button.pack()

window.mainloop()
