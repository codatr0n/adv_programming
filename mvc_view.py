import mvc_controller as controller
from tkinter import *

def show_data(data):
    if type(data) == list:
        for row in data:
            print('{}: {}'.format(data[0][1], row[1]))
            print('{}: {}'.format(data[0][2], row[2]))
            print('{}: {}'.format(data[0][3], row[3]))
            print('{}: {}'.format(data[0][4], row[4]))
            print('{}: {}'.format(data[0][5], row[5]))
            print('{}: {}'.format(data[0][6], row[6]))
            print()


def start_view(data):

    data = data
    
    root = Tk() # create a Tk root window

    w = 800 # width for the Tk root
    h = 650 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.mainloop() # starts the mainloop 
