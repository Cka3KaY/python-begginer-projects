# import required module
from playsound import playsound

from tkinter import *  
import tkinter as tk


def note_1():
    playsound('Notes/1.wav')
    Notes.append("C")
def note_2():
    playsound('Notes/2.wav')
    Notes.append("D")
def note_3():
    playsound('Notes/3.wav')
    Notes.append("E")
def note_4():
    playsound('Notes/4.wav')
    Notes.append("F")
def note_5():
    playsound('Notes/5.wav')
    Notes.append("G")
def note_6():
    playsound('Notes/6.wav')
    Notes.append("A")
def note_7():
    playsound('Notes/7.wav')
    Notes.append("C")
def note_8():
    playsound('Notes/8.wav');



w = Label(root, text=Notes, font=("Comic Sans", 20))
w.pack()

b1 = tk.Button(root, text="         C         ", command=note_1, font=("Comic Sans", 20),)
b1.pack()
b2 = tk.Button(root, text="         D         ", command=note_2, font=("Comic Sans", 20),)
b2.pack()
b3 = tk.Button(root, text="         E         ", command=note_3, font=("Comic Sans", 20),)
b3.pack()
b4 = tk.Button(root, text="         F         ", command=note_4, font=("Comic Sans", 20),)
b4.pack()
b5 = tk.Button(root, text="         G         ", command=note_5, font=("Comic Sans", 20),)
b5.pack()   
b6 = tk.Button(root, text="         A         ", command=note_6, font=("Comic Sans", 20),)
b6.pack()
b7 = tk.Button(root, text="         B         ", command=note_7, font=("Comic Sans", 20),)
b7.pack()
b8 = tk.Button(root, text="         C         ", command=note_8, font=("Comic Sans", 20),) 
b8.pack()









root.mainloop() # MUST BE AT THE END!!!!!
