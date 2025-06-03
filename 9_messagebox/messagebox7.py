from tkinter import *
from tkinter import messagebox  # import messagebox library

#7. ASK QUESTION

def click():
    

    answer = messagebox.askquestion(title='Ask Question?',
                        message='Are you over 18 years?')
    if(answer == 'yes'):
        print('You are an adult!')
    else:
        print('You are a minor!')
       

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
