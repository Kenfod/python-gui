from tkinter import *
from tkinter import colorchooser  #submodule

def click():

    window.config(bg=colorchooser.askcolor()[1])  #change background color

window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


button = Button(text='Click Here !', 
                command=click)
button.pack()


window.mainloop()
