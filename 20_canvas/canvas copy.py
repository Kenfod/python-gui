from tkinter import *

#   canvas = widget that is used to draw graphs, plots, images in a window.

#15 PROJECT 1- DRAWING A POKEMON

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

canvas = Canvas(window, height=500, width=500)

# canvas.create_line(0,0,500,500, fill="blue", width=5)
# canvas.create_line(0,500,500,0, fill="red", width=5)

# canvas.create_rectangle(50,50,250,250, fill="purple")

# points = [250,0,500,500,0,500]

# canvas.create_polygon(points, fill="yellow", outline="black", width=5)

# canvas.create_arc(0,0,500,500, fill="green")

# canvas.create_arc(5,5,490,490, style=CHORD, fill="grey")

# canvas.create_arc(5,5,490,490, style=PIESLICE)

# OR

# canvas.create_arc(5,5,490,490, style=PIESLICE, start=0)

# canvas.create_arc(5,5,490,490, style=PIESLICE, start=90)

# canvas.create_arc(5,5,490,490, style=PIESLICE, start=180)

# canvas.create_arc(5,5,490,490, style=PIESLICE, start=270)

# canvas.create_arc(5,5,490,490, style=PIESLICE, start=270, extent=180)

canvas.create_arc(5,5,490,490, fill="red",extent=180, width=5)

canvas.create_arc(5,5,490,490, fill="white",extent=180, start=180, width=5)

canvas.create_oval(190,190,310,310, fill="white", width=5)

canvas.pack()

window.mainloop()
