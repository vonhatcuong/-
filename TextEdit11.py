import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import subprocess, webbrowser,configparser
import sys
import webbrowser
from tkinter.scrolledtext import ScrolledText


class TextEdit:
    def __init__(self,root):
        root.title(self.__class__.__name__)
        root.geometry('300x50')
        root.option_add('*tearOff', FALSE)
        menu = Menu(root)

        menuFile = Menu(menu)
        menu.add_cascade(menu=menuFile,label='ファイル(F)', underline=5)
        menuFile.add_command(label='新規(N)', underline=3, command=self.menuFileNew)
        menuFile.add_command(label='開く(O)',underline=3, command=self.menuFileOpen)
        menuFile.add_command(label='保存(S)',underline=3, command=self.menuFileSave)
        menuFile.add_command(label='名前を付けてシフトJISで保存(A)',underline=16, command=self.menuFileSaveAsSjis)
        menuFile.add_command(label='名前を付けてUTF-8で保存(U)',underline=15, command=self.menuFileSaveAsUtf8)
        menuFile.add_command(label='終了(X)',underline=3, command=self.menuFileExit)

        menuHelp = Menu(menu)
        menu.add_cascade(menu=menuHelp,label='ヘルプ(H)', underline=4)
        menuHelp.add_command(label='Webサイトを開く(W)',underline=10, command=self.menuHelpOpenWeb)


        text = Text(root)
        text.pack(expand=1, fill=BOTH)
        text = ScrolledText(root, width=30, height=10)
        text.pack(expand=1, fill=BOTH)



        menuHelp.add_separator()
        menuHelp.add_command(label='バージョン情報(V)',
        underline=8, command=self.menuHelpVersion)
        root['menu'] = menu
        ttk.Button(root, text="押してください！", command=self.Button1Clicked).pack()


    def Button1Clicked(self):
        messagebox.showinfo(root.title(),"ありがとうございます！")

    def menuFileExit(self):
        cp = configparser.ConfigParser()
        cp['Client'] = {'Height': str(root.winfo_height()),'Width': str(root.winfo_width())}
        with open(self.__class__.__name__ +'.ini', 'w') as f:
            cp.write(f)
        root.destroy()

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += ' Version 0.01(2021/07/28)\n'
        s += '©2021 Naohide Mori\n'
        s += 'with Python ' + sys.version
        messagebox.showinfo(
        self.__class__.__name__, s)

    def menuHelpOpenWeb(self):
         subprocess.Popen(['start', 'readme.txt'],shell=True)

    def menuFileNew(self):
        pass
    def menuFileOpen(self):
        pass
    def menuFileSave(self):
        pass
    def menuFileSaveAsSjis(self):
        pass
    def menuFileSaveAsUtf8(self):
        pass





root = tk.Tk()
TextEdit(root)
root.mainloop()
