'''
TODO:
Fix black blinking while refreshing text
Write endgame function
'''
import tkinter

# Loading misc module. Idk how to do it better. Python is shit in this


def load_misc_module():
    import sys
    sys.path.append(sys.path[0] + '/../tools')
    import misc
    return misc


misc = load_misc_module()

# Configuration main values
color_bg = '#3E4149'
color_white = 'white'

score = 0
seconds_constant = 10
seconds = seconds_constant
lives = 10

# Initing window
root = tkinter.Tk()
root.title('VASHE_POHUI')
root.geometry('500x500')
root.resizable(False, False)
root.configure(background=color_bg)

# Initing frame
frame = tkinter.Frame(root)
frame.grid(row=0, column=0)
frame.pack(expand=True)

# Initing labels
label_gamemode = tkinter.Label(
    text="Game mode: UPH", bg=color_bg, fg=color_white)
label_time = tkinter.Label(
    text="Time left: 00:10", bg=color_bg, fg=color_white)
label_score = tkinter.Label(
    text="Your score: 0", bg=color_bg, fg=color_white)
label_gamemode.pack()
label_time.pack()
label_score.pack()

# Gen game field
grid_size = 7
game_field = misc.random_grid(
    grid_size, 100, True, False, False)


def main(height=5, width=5):
    global game_field
    for x in range(width):
        row_start = x * width  # Too lazy to explain it. Dm Stefan for explanation
        for y in range(height):
            item = game_field[0][row_start + y]
            btn = tkinter.Button(frame,  text=item, width=2, height=1,
                                 highlightbackground='#3E4149',  activebackground='black')
            btn.grid(column=y, row=x)
            btn['command'] = lambda btn = btn: click(btn)
    return frame


def click(button):
    global seconds_contant, seconds, score, lives
    if int(button['text']) in game_field[1]:
        button['text'] = '✅'
        score += 1
        seconds = seconds_constant
    else:
        button['text'] = '❌'
        lives -= 1
    button['state'] = 'disable'
    label_score.config(text=f'Your score: {score}')


def timer():
    '''
    Player has seconds_contant seconds to guess a number, if not game will end
    If player guesses timer is restored
    '''
    global seconds
    seconds_to_disp = f"0{seconds}" if len(str(seconds)) == 1 else f"{seconds}"
    label_time.config(
        text=f"Time left: 00:{seconds_to_disp}", bg=color_bg, fg=color_white)
    if seconds == 0:
        return endgame()
    seconds -= 1

    root.after(1000, timer)


def endgame():
    print('Endgame triggered')


main(grid_size, grid_size)
timer()
tkinter.mainloop()
