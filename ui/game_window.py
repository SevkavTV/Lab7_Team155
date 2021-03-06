import tkinter


def load_misc_module():
    import sys
    sys.path.append(sys.path[0] + '/tools')
    import misc
    return misc


misc = load_misc_module()

# Configuration main values
color_bg = '#3E4149'
color_white = 'white'

# Game config, should be passed from start menu
seconds_constant = 10
lives_constant = 3
mode_strings = ['Ulam', 'Happy', 'Prime']
game_mode = []

# Dynamic ingame values
score = 0
seconds = seconds_constant


def number_to_hearts(n: int) -> str:
    '''
    Create a string with 'n' hearts
    '''
    return ''.join(['❤️' for _ in range(n)])


lives = lives_constant

root = None
frame = None
label_gamemode = None
label_time = None
label_score = None
label_lives = None
grid_size = None
game_field = None
game_status = None
timer_running = True
timer_obj = None


def init():
    '''
    Initiliaze a window with game field and all other labels
    '''
    global root, frame, label_gamemode, label_time, label_score, label_lives, timer_running
    # Initing window
    timer_running = True
    root = tkinter.Tk()
    root.title('HACKtheBOB')
    root.iconbitmap("among_us.ico")
    root.geometry('500x500')
    root.resizable(False, False)
    root.configure(background=color_bg)

    # Initing frame
    frame = tkinter.Frame(root)
    frame.grid(row=0, column=0)
    frame.pack(expand=True)
    # Initing labels, game mode, grid
    create_grid()

    game_string_list = []
    for index, item in enumerate(game_mode):
        if item == 1:
            game_string_list.append(mode_strings[index])

    label_gamemode = tkinter.Label(
        text=f"Password type: {' | '.join(game_string_list)}", bg=color_bg, fg=color_white)
    label_time = tkinter.Label(
        text=f"Time left: {seconds}", bg=color_bg, fg=color_white)
    label_score = tkinter.Label(
        text="Your progress: 0", bg=color_bg, fg=color_white)
    label_lives = tkinter.Label(
        text=f"Lives: {number_to_hearts(lives)}", bg=color_bg, fg=color_white)
    label_gamemode.pack()
    label_time.pack()
    label_score.pack()
    label_lives.pack()


def main(height=5, width=5):
    global game_field
    for x in range(width):
        row_start = x * width  # Too lazy to explain it. Dm Stefan for explanation
        for y in range(height):
            item = game_field[0][row_start + y]
            btn = tkinter.Button(frame,  text=item, width=2, height=1,
                                 highlightbackground='#3E4149',  activebackground='black')
            btn.grid(column=y, row=x)
            btn.bind(f'<Button>', click)
    return frame


def reset_timer():
    '''
    Update timer
    '''
    global seconds
    seconds = seconds_constant


def substact_life():
    '''
    Subtract one life. If they are over, you lose 
    '''
    global lives
    lives -= 1
    reset_timer()
    label_lives.config(text=f'Lives: {number_to_hearts(lives)}')
    if lives == 0:
        return endgame('lose')


def add_point():
    '''
    Add one point to your current point value
    '''
    global score, seconds
    score += 1
    seconds = seconds_constant
    label_score.config(text=f'Your score: {score}')


def click(event):
    '''
    Handle click on the board game and determine whether user clicked the right number.
    '''
    button = event.widget
    if event.num == 1 and int(button['text']) in game_field[1]:
        game_field[1].remove(int(button['text']))
        button['text'] = '✅'

        if len(game_field[1]) == 0:
            endgame('win')

        add_point()
    elif event.num == 2 and int(button['text']) not in game_field[1]:
        button['text'] = '❌'
        reset_timer()
    else:
        button['text'] = '💀'
        substact_life()
    button['state'] = 'disable'


def timer():
    global timer_obj
    '''
    Player has seconds_contant seconds to guess a number, if not game will end
    If player guesses timer is restored
    '''
    global seconds
    seconds_to_disp = f"0{seconds}" if len(str(seconds)) == 1 else f"{seconds}"
    label_time.config(
        text=f"Time left: 00:{seconds_to_disp}")
    if seconds == 0:
        substact_life()
        reset_timer()
    else:
        seconds -= 1

    if timer_running:
        timer_obj = root.after(1000, timer)
    else:
        root.destroy()
        import results_window
        results_window.status = game_status
        results_window.init()


def endgame(status):
    '''
    Function that change parametres for end of the game.
    '''
    global game_status, timer_running
    timer_running = False
    game_status = status


def create_grid():
    '''
    Create game field by data from the start screen.
    '''
    global grid_size, game_field

    grid_size = 7
    game_field = misc.random_grid(
        grid_size, 100, game_mode[0], game_mode[1], game_mode[2])


def start_window():
    '''
    Main function to build screen and timer.
    '''
    init()
    main(grid_size, grid_size)
    timer()
    tkinter.mainloop()


if __name__ == '__main__':
    start_window()
    # tkinter.mainloop()
