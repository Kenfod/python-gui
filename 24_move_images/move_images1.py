from tkinter import *

#1. MOVE WIDGET WITHIN A WINDOW

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)


def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="white")


window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


myimage = PhotoImage(file='kermit2.png')
label = Label(window, image=myimage)
label.place(x=0, y=0)


window.mainloop()
