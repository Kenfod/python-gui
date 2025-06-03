from tkinter import *
from tkinter import messagebox  # import messagebox library

#4. ASK OK CANCEL

def click():
    
    if messagebox.askokcancel(title='Ask Ok cancel?!',
                        message='Do you want to try again!'):
        print('You clicked the Button again!')
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
