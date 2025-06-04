from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#5 DRAWING A POLYGON-by passing a list of points.

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

points = [250,0,500,500,0,500]

canvas.create_polygon(points, fill="yellow", outline="black", width=5)

canvas.pack()

window.mainloop()
