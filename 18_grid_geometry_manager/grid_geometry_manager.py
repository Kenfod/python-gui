from tkinter import *

#   grid() = Geometry manager that orgarnizes widgets in atable-like strucutre in a parent

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

titleLabel = Label(window, text="Enter your Info", font=("Arial",25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name: ", width=20, bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last Name: ", bg="green").grid(row=2,column=0)
lasttNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="E-mail: ", width=20, bg="blue").grid(row=3,column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)


window.mainloop()
