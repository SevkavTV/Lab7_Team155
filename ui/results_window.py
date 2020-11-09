from tkinter import *
from PIL import ImageTk, Image


status = ''

root = None


def init():
    '''
    Initiliaze a window with needable picture
    '''
    global status, root
    root = Tk()
    root.geometry("500x500")
    root.resizable(False, False)
    root.title('HACKtheBOB')
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

    start_button = Button(root, text="TRY AGAIN", padx=20,
                          pady=5, command=return_to_menu)
    start_button.place(x=200, y=400)

    root.mainloop()


def return_to_menu():
    '''
    Transition to the start screen.
    '''
    root.destroy()
    import start_window
    start_window.init()
