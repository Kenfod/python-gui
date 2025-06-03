from tkinter import *

#   listbox = A listing of selectable text items within it's own container.

#B. TO SELECT MORE THAN ONE ITEM

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

listbox = Listbox(window, 
                  bg="#f7ffde",
                  font=("Constantia",30),
                  width=13,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Hotdog")
listbox.insert(2,"Hamburger")
listbox.insert(3,"Pizza")
listbox.insert(4,"Masala chips")
listbox.insert(5,"Fired chicken")
listbox.insert(6,"Juice")

listbox.config(height=listbox.size())

entryBox =Entry(window)
entryBox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

window.mainloop()
