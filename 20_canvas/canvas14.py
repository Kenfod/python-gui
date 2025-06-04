from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#14 PROJECT 1- DRAWING A POKEMON

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

canvas.create_arc(5,5,490,490, fill="red",extent=180, width=5)

canvas.create_arc(5,5,490,490, fill="white",extent=180, start=180, width=5)

canvas.create_oval(190,190,310,310, fill="white", width=5)

canvas.pack()

window.mainloop()
