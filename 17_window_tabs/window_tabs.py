from tkinter import *
from tkinter import ttk


window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
#window.config(background="cyan")


notebook = ttk.Notebook(window)  #widget that manages a colletion of windows/displays.

tab1 = Frame(notebook)  #New frame for Tab 1
tab2 = Frame(notebook)  #New frame for Tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True,   #expand is used to fill any space not otherwise used.
              fill="both")   #fill is use to fill space on x and y axis.

Label(tab1, text='Hi, this is Tab 1', width=50, height=25).pack()
Label(tab2, text='Bye, this is Tab 2', width=50, height=25).pack()

window.mainloop()
