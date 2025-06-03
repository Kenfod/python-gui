from tkinter import *

#   text widget = funstions like a text area; you can enter multiple lines of text.

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


text = Text(window, 
            bg='light yellow',
            font=('Ink Free', 20),
            height=8,
            width=30,
            padx=20,
            pady=10,
            fg='blue')
text.pack()


button = Button(window, 
                text='Submit', 
                command=submit)
button.pack()


window.mainloop()
