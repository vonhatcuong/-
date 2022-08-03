import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *


def Button1Clicked():
    messagebox.showinfo(root.title(),"ありがとうございます！")


root = tk.Tk()

root.title("TextEdit")
root.geometry('300x500')

ttk.Button(root, text="Greet", command=Button1Clicked).pack()

root.mainloop()
