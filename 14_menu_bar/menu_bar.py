from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You have cut some text!")

def copy():
    print("You have copied some text!")

def paste():
    print("You have pasted some text!")

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="close.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu =Menu(menubar, tearoff=0, font=("MV Boli",10))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage,  compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage,  compound=LEFT)


editMenu =Menu(menubar, tearoff=0, font=("MV Boli",10))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
# fileMenu.add_separator()
editMenu.add_command(label="Paste", command=paste)


window.mainloop()
