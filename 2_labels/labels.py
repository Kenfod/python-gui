from tkinter import *

#   label = an area widget that holds text and/or an image within a window.


window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

photo = PhotoImage(file='2_labels\\ipad.png')

label=Label(window, text="Hello Kay!",
            font=('Arial',40,'bold'),
            fg='#00FF00',
            bg='black',
            relief=RAISED,
            bd=10,
            padx=20,
            pady=10,
            image=photo,
            compound='bottom')
label.pack()

#label.place(x=0, y=0)


window.mainloop()
