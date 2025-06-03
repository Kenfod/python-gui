from tkinter import *
from tkinter import messagebox  # import messagebox library

#1. MESSAGE BOX

def click():
    messagebox.showinfo(title='Message Box',
                        message='Button Clicked!!')

        
window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


button = Button(window, 
                command=click,
                text='Click Here!')
button.pack()


window.mainloop()
