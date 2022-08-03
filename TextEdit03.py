import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *

class TextEdit:
    def __init__(self,root):
        root.title(self.__class__.__name__)
        root.geometry('300x50')
        ttk.Button(root, text="押してください！", command=self.Button1Clicked).pack()


    def Button1Clicked(self):
        messagebox.showinfo(root.title(),"ありがとうございます！")


root = tk.Tk()
TextEdit(root)

root.mainloop()
