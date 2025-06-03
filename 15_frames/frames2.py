from tkinter import *

#   frame = A rectangular container to group and hold widgets.


window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


# button = Button(window, text="W", font=("Consolas", 25), width=3)
# button.pack()

# SEE ALTERNATIVE SHORT CODE FOR THE ABOVE:

frame = Frame(window, bg="pink", bd=5, relief=RAISED)
frame.pack(side=BOTTOM)  #To posiyon the frame at the bottom.

Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
