from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#3 DRAWING A RECTANGLE

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

canvas.create_rectangle(50,50,250,250, fill="purple")

canvas.pack()

window.mainloop()
