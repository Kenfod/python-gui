from tkinter import *
from tkinter import messagebox  # import messagebox library

#2. SHOW WARNING

def click():
    
    messagebox.showwarning(title='WARNING!!',
                        message='This a DANGER ZONE!')
        

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
