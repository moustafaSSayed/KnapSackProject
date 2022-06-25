import sys

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def run():
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

    # To start our window
if __name__ == '__main__':
    import FirstScreen
    FirstScreen.vp_start_gui()




