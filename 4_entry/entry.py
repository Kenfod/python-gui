from tkinter import *

#   entry widget = text box that accepts a single line of user input.

def submit():
    username = entry.get()
    print("Hello "+username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()  

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

entry = Entry(window, 
              font=("Arial",50),
              fg="#00ff00",
              bg="black")

# entry.insert("Spongebob")
# entry.config(show="*")
# entry.config(state=DISABLED)

entry.pack(side=LEFT)

submit_button = Button(window, 
                       text="Submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, 
                       text="Delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, 
                       text="Backspace",
                       command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()

