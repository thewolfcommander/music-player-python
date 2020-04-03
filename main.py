"""
Developed by Manoj Tyagi
"""

import os
import tkinter.messagebox

from tkinter import *
from tkinter import filedialog

from pygame import mixer

root = Tk()


# Creating the menubar
menubar = Menu(root)
root.config(menu=menubar)

# CReating the submenu
subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)



def about_us():
    tkinter.messagebox.showinfo('About Sim', 'This is a music player built using Python Tkinter by Manoj Tyagi')


subMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us"), command=about_us)