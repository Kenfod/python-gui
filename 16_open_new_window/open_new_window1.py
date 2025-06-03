from tkinter import *

def create_window():
    new_window = Toplevel()  #Toplevel()-is a new window 'on top' of other windows. Linked to a 'bottom' window.

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


Button(window, text="Create New Window", command=create_window).pack()


window.mainloop()
