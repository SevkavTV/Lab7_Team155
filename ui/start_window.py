from tkinter import *
from PIL import ImageTk, Image


def start_game():
    root.destroy()
    import game_window
    game_window.lives = 3
    game_window.game_mode = [var1.get(), var2.get(), var3.get()]
    game_window.start_window()


root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("HACKtheBOB")
root.iconbitmap("among_us.ico")

my_image = ImageTk.PhotoImage(Image.open("fr1.gif"))
my_label = Label(root, image=my_image)
my_label.place(x=0, y=0)


start_button = Button(root, text="LOG IN", padx=50, command=start_game)
start_button.pack(pady=50)

frame = LabelFrame(root, text="Choose password type")
frame.pack()

var1 = IntVar()
option1 = Checkbutton(frame, text="Ulam's numbers", variable=var1)
option1.pack()

var2 = IntVar()
option2 = Checkbutton(frame, text="Happy numbers", variable=var2)
option2.pack()

var3 = IntVar()
option3 = Checkbutton(frame, text="Prime numbers", variable=var3)
option3.pack()

button_quit = Button(root, text="Exit", padx=20, pady=5, command=root.quit)
button_quit.pack(pady=100)


root.mainloop()
