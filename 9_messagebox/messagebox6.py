from tkinter import *
from tkinter import messagebox  # import messagebox library

#6. ASK YES NO

def click():
    
    if messagebox.askyesno(title='Ask Yes or No?',
                        message='Do you want to continue?'):
        print('Congratulations! You proceed to the next stage!')
    else:
        print('Sorry! You have terminated the process!')

        

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
