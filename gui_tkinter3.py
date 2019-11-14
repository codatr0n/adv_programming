from tkinter import *


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def set_bg_color(self):
    # print(red.get(), green.get(), blue.get())
    master.configure(bg=_from_rgb((red.get(), green.get(), blue.get())))


master = Tk()

red = IntVar()
red.set(255)
green = IntVar()
green.set(255)
blue = IntVar()
blue.set(255)

master.configure(bg=_from_rgb((red.get(), green.get(), blue.get())))
master.geometry("500x500")


w = Scale(master, from_=0, to=255, orient=HORIZONTAL, variable=red)
w.bind("<ButtonRelease-1>", set_bg_color)
w.pack()

w = Scale(master, from_=0, to=255, orient=HORIZONTAL, variable=green)
w.bind("<ButtonRelease-1>", set_bg_color)
w.pack()

w = Scale(master, from_=0, to=255, orient=HORIZONTAL, variable=blue)
w.bind("<ButtonRelease-1>", set_bg_color)
w.pack()

mainloop()
