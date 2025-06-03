from tkinter import *
from tkinter import messagebox  # import messagebox library

#3. SHOW ERROR

def click():

    messagebox.showerror(title='Error Message!',
                        message='Please try again!')
        

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
