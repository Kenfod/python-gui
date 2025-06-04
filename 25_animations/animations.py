from tkinter import *
import time

WIDTH=500
HEIGHT=500

xVelocity =5
yVelocity =2


window = Tk()

window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


background_photo = PhotoImage(file='pixabay2.png')
background = canvas.create_image(0,0, image=background_photo, anchor=NW)


photoimage = PhotoImage(file='ufo.png')
myimage = canvas.create_image(0,0, image=photoimage, anchor=NW)


image_width = photoimage.width()
image_height = photoimage.height()

while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)

    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity

    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(myimage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
