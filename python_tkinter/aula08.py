def submit():
    food_list = []
    for index in listbox.curselection():
        food_list.insert(index, listbox.get(index))
    print("You have ordered:")
    for index in food_list:
        print(f" → {index.capitalize()}")

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

from tkinter import *

# listbox = um widget que exibe uma lista de itens de texto e permite o usuário selecionar um ou mais desses itens.

window = Tk()

listbox = Listbox(
    window,
    bg="#f7ffde",
    font=("Constantia", 35),
    width=12,
    selectmode=MULTIPLE
)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(
    window,
    text="submit",
    command=submit
)
submitButton.pack()

addButton = Button(
    window,
    text="add",
    command=add
)
addButton.pack()

deleteButton = Button(
    window,
    text="delete",
    command=delete
)
deleteButton.pack()

window.mainloop()
