from tkinter import *

#   button = when clicked, it performs an action.


window = Tk()  
window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

count=0

def click():
    global count
    count+=1
    print(count)

    #print("You clicked the button times!")

photo = PhotoImage(file='thumb-up.png')

button = Button(window, 
                text='Click here!',
                command=click,
                font=('Comic Sans',30),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE,
                image= photo,
                compound='top')
button.pack()


window.mainloop()
