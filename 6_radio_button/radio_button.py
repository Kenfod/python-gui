from tkinter import *

#   radio button = is similar to acheck box(check button), but, you can select only one option from a group of options.

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("Huh?")

    

window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hot-dog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons.
                              variable=x,  #groups radio buttons together if they share the same variable.
                              value=index,  #assigns each radio button a different value. 
                              padx=20,
                              pady=10,
                              font=("Impact", 40),
                              image = foodImages[index],  #adds image to radio buttons.
                              compound=LEFT,  #adds image & text (left-side)
                              indicatoron=0,  #eliminates the circle indicators
                              width=375,  #sets width of radio buttons.
                              command=order  #sets command of radio button to function.
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
