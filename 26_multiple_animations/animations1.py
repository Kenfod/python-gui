from tkinter import *
from Ball import *
import time


window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


WIDTH=500
HEIGHT=500


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 2, 1, "brown")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "green")
basket_ball = Ball(canvas, 0, 0, 120, 5, 2, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
