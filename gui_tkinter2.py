from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("500x500")
mb = Menubutton(top, text="condiments")
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)
mb.pack()
top.mainloop()
