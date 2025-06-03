from tkinter import *

def create_window():
    new_window = Tk()  #Tk()- is a new independent window.
                             
window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


Button(window, text="Create New Window", command=create_window).pack()


window.mainloop()
