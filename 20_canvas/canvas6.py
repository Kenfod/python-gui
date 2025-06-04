from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#6 DRAWING AN ARC-1

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

canvas.create_arc(0,0,500,500, fill="green")

canvas.pack()

window.mainloop()
