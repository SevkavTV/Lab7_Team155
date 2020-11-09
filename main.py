
def load_start_window_module():
    import sys
    sys.path.append(sys.path[0] + '/ui')
    import start_window
    return start_window


start_window = load_start_window_module()
start_window.init()
