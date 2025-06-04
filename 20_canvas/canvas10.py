from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#10 DRAWING A PIE SLICE-2

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

canvas.create_arc(5,5,490,490, style=PIESLICE, start=90)

canvas.pack()

window.mainloop()
