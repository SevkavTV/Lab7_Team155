import tkinter

window2 = tkinter.Tk()
window2.geometry('500x500')
# window1 = game_window.get_window()
# window2.withdraw()
frame = tkinter.Frame(window2)
frame.grid(row=1, column=1)
frame.pack(expand=True)
start_btn = tkinter.Button(frame, text="123", fg='black')
start_btn.grid(column=1, row=1)


def click():
    window2.destroy()  # Close current window
    import game_window  # Import game window
    game_window.lives = 10  # Setting all game vars
    game_window.start_window()  # Launchung game window


start_btn['command'] = click


tkinter.mainloop()
