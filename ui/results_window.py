from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Results")
root.iconbitmap("among_us.ico")


def init():
    image = Image.open('you_lost.png')
    image = image.resize((500, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.place(x=0, y=0)

    start_button = Button(root, text="Go to menu", padx=20,
                          pady=5, command=return_to_menu)
    start_button.place(x=200, y=400)


def return_to_menu():
    root.destroy()
    import game_window
    game_window.lives = 10
    game_window.game_mode = [var1.get(), var2.get(), var3.get()]
    game_window.start_window()


if __name__ == '__main__':
    init()
    mainloop()
