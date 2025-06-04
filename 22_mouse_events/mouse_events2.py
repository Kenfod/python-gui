from tkinter import *

#2. MOUSE SCROLL-WHEEL PRESSED

def perform(event):
    print("Mouse co-ordinates: "+str(event.x)+","+str(event.y))

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


window.bind("<Button-2>", perform)  

window.mainloop()
