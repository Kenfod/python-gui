from tkinter import *

def create_window():
    new_window = Tk()  #Tk()- is a new independent window.

    old_window.destroy()  #closes the old window.
                             
old_window = Tk()


old_window.geometry("500x500")
old_window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
old_window.iconphoto(True, icon)
old_window.config(background="cyan")


Button(old_window, text="Create New Window", command=create_window).pack()


old_window.mainloop()
