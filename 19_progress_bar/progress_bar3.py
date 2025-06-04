from tkinter import *
from tkinter.ttk import *
import time

#VERTICAL ORIENT DISPLAY

def start():
    GB = 10
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.5)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()


window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=VERTICAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()

taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
