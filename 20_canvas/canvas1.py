from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#1 DRAWING A LINE

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)
canvas.create_line(0,0,500,500, fill="blue", width=5)
canvas.create_line(0,500,500,0, fill="red", width=5)
canvas.pack()

window.mainloop()
