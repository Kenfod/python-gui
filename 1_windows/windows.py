from tkinter import *

#   widget = GUI elements such as buttons, textboxes, labels, images.
#   #window = serves as a container to hold or contain these widgets.

window = Tk()  #instantiate an instance of a window

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

window.mainloop() #place window on computer screen, listen for events.
