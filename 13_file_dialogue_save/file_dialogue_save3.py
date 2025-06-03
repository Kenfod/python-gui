from tkinter import *
from tkinter import filedialog

#USING THE CONSOLE WINDOW TO WRITE A MESSAGE

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\Admin\\Desktop\\python_gui\\12_file_dialogue_open', 
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text File','.txt'),
                                        ('HTML File','.html'),
                                        ('All Files', '*.*'),
                                    ])
    # if file is None:
    #     return
    
    #filetext = str(text.get(1.0, END))
    filetext = input('Enter your message here: ')   #use this if you want to use console.
    file.write(filetext)
    file.close()

window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


button = Button(text='Save File', 
               command=saveFile)
button.pack()

text = Text(window)
text.pack()


window.mainloop()
