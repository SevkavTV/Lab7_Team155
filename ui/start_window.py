from tkinter import *
window = Tk()
TK_SILENCE_DEPRECATION = 1
window.title('A POOO')
window.geometry('500x500+500+200')
window.resizable(False, False)
start_game_label = Label(window, text="Hello Tkinter!")
start_game_label.pack()

window.mainloop()
