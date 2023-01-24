from tkinter import *
from tkinter.ttk import *

from time import strftime 

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    