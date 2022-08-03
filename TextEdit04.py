import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *

class TextEdit:
    def __init__(self,root):
        root.title(self.__class__.__name__)
        root.geometry('300x50')
        root.option_add('*tearOff', FALSE)
        menu = Menu(root)
        menuFile = Menu(menu)
        menu.add_cascade(menu=menuFile,
        label='ファイル(F)', underline=5)
        menuFile.add_command(label='終了(X)',
        underline=3, command=self.menuFileExit)
        root['menu'] = menu
        ttk.Button(root, text="押してください！", command=self.Button1Clicked).pack()


    def Button1Clicked(self):
        messagebox.showinfo(root.title(),"ありがとうございます！")
    def menuFileExit(self):
        root.destroy()


root = tk.Tk()
TextEdit(root)
root.mainloop()
