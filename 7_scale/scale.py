from tkinter import *

def submit():
    print("the temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

hotImage = PhotoImage(file='hot.png')
hotLabel =Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, 
              from_=100, 
              to_=0,
              length=550,
              orient=VERTICAL, #orientation of the scale.
              font=('Consolas',20),
              tickinterval=10,  #adds numeric indicators for value.
              #showvalue=0,
              resolution=5,  #increment of slider
              troughcolor='#69FAFF',
              fg='#FF1C00',
              bg='#111111')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])  #set current value of the slider.

scale.pack()

coldImage = PhotoImage(file='cold.png')
coldLabel =Label(image=coldImage)
coldLabel.pack()

button = Button(window, 
                text='submit', 
                command=submit)
button.pack()

window.mainloop()
