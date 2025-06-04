from tkinter import *

def perform(event):
    #print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


window.bind("<Key>", perform)

label = Label(window, font=("Helvetica", 50))
label.pack()


window.mainloop()
