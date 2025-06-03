from tkinter import *
from tkinter import messagebox  # import messagebox library

#5. ASK RETRY CANCEL

def click():

    if messagebox.askretrycancel(title='Retry or cancel?',
                        message='Do you want to retry?'):
        print('You clicked the Retry Button!')
    else:
        print('You cancelled it !')

        

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
