# função retirada de https://pythonprogramming.altervista.org/how-to-center-your-window-with-tkinter-in-python/

def center_screen(app, window_width, window_height):
    global screen_height, screen_width, x_cordinate, y_cordinate
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))