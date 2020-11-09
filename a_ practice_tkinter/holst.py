# show game grid
from tkinter import *

root = Tk()
root.title('POHUI')
root.geometry('500x500')
root.resizable(False, False)
frame=Frame(root)
frame.grid(row=0, column=0)
root.grid_rowconfigure(0, weight=5)
root.grid_columnconfigure(0, weight=5)

active="red"
default_color="white"

def main(height=5,width=5):
    for x in range(width):
        for y in range(height):
            btn = Button(frame, bg=default_color, text=(width*x + y+1), width=2, height=1)
            btn.grid(column=y, row=x)

            btn["command"] = lambda btn=btn: click(btn)


    return frame

def click(button):
    print(button['text'])

w = main(15, 15)
mainloop()