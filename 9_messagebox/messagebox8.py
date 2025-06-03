from tkinter import *
from tkinter import messagebox  # import messagebox library

#8. ASK YES NO CANCEL

def click():

    answer = messagebox.askyesnocancel(title='Yes No Cancel!',
                        message='Do you know Python programming?',
                        # icon='warning',
                        # icon='info',
                        # icon='error'
                        )
    if(answer==True):
        print('Congratulations! You are a Python programmer!')
    elif(answer==False):
        print('Sorry! You are not a Python programmer, but its not too late to start now!')
    else:
        print('Not interested??')
        

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
