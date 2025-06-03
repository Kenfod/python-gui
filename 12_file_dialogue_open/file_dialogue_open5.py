from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()

    if not filepath:
        print("No file selected.")
        return
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as file:
            content = file.read()
            print(content.encode('utf-8', errors='replace').decode('utf-8'))
    except Exception as e:
        print(f"Failed to read file: {e}")



    #     with open(filepath, 'r', encoding='utf-8') as file:
    #         print(file.read())
    # except UnicodeDecodeError:
    #     print("Failed to read file: encoding issue. Try using a different encoding like 'latin-1'.")
    # except Exception as e:
    #     print(f"Failed to read file: {e}")



    #     with open(filepath, 'r', encoding='utf-8') as file:
    #         print(file.read())
    # except Exception as e:
    #     print(f"Failed to read file: {e}")


    #print(filepath)
    # file = open(filepath,'r')
    # print(file.read())
    # file.close()


window = Tk()


window.geometry("500x500")
window.title("Kay Inc.")
icon = PhotoImage(file='1_windows\\jipange.png')
window.iconphoto(True, icon)
window.config(background="cyan")


button = Button(text='Open File', 
               command=openFile)
button.pack()


window.mainloop()
