from tkinter import *

# where x variable is a boolean

def display():
    if(x.get()):
        print("You agree!")
    else:
        print("You don't agree!")


window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

x = BooleanVar()

python_photo =PhotoImage(file='python.png')

check_button = Checkbutton(window, 
                           text="I agree to the conditions", 
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial,20'),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=20,
                           pady=10,
                           image=python_photo, 
                           compound='left')

check_button.pack()

window.mainloop()
