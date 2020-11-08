from tkinter import *
from PIL import ImageTk, Image

root = Tk()

status = ''


def init():
    global status

    root.geometry("500x500")
    root.resizable(False, False)
    root.title("Results")
    root.iconbitmap("among_us.ico")
    image = None
    if status == 'win':
        image = Image.open('you_won.png')
    else:
        image = Image.open('you_lost.png')
    image = image.resize((500, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.place(x=0, y=0)

    start_button = Button(root, text="Go to menu", padx=20,
                          pady=5, command=return_to_menu)
    start_button.place(x=200, y=400)

    root.mainloop()


def return_to_menu():
    print('Go to menu')
