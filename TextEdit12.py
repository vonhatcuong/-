import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog
import subprocess, webbrowser,configparser
import sys
import os
from tkinter.scrolledtext import ScrolledText


class TextEdit:
    def __init__(self,root):
        root.title(self.__class__.__name__)
        root.geometry('525x350')
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

        _textFilename = ''
        @property
        def textFilename(self):
          return self._textFilename

        @textFilename.setter
        def textFilename(self, value):
            self._textFilename = value
            if value == '':
                root.title(self.__class__.__name__)
                self.menuFile.entryconfigure('保存(S)', state=DISABLED)
            else:
                s=os.path.basename(value)
                if self.isSjis(s):
                    s += ' (JIS)'
                else:
                    s += ' (UTF-8)'
                root.title(s)
                self.menuFile.entryconfigure('保存(S)', state=NORMAL)
                self.directory = os.path.dirname(value)

        self.text = ScrolledText(root)
        self.text.pack(expand=1, fill=BOTH)
        self.fileTypes = [('テキストファイル', '*.txt'), ('すべてのファイル', '*')]
        self.directory = os.getenv('HOMEDRIVE') \
        + os.getenv('HOMEPATH') + '\\Documents'
        clientHeight = '50'
        try:
            cp.read(self.__class__.__name__ + '.ini')
            clientHeight = cp['Client']['Height']
            clientWidth = cp['Client']['Width']
            self.directory = cp['File']['Directory']
        except:
            pass

        menuHelp.add_separator()
        menuHelp.add_command(label='バージョン情報(V)',
        underline=8, command=self.menuHelpVersion)
        root['menu'] = menu
        self.menuFileNew()
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
        self.isSjis = TRUE
        self.textFilename = ''
        self.text.delete('1.0', 'end')

    def menuFileOpen(self):
        filename = filedialog.askopenfilename(filetypes=self.fileTypes,initialdir=self.directory)
        if not filename:
            return
        newText = ''
        try:
            f = open(filename, 'r')
            newText = f.read()
            self.isSjis = TRUE
        except:
            f = open(filename, 'r', encoding='UTF-8')
            newText = f.read()
            self.isSjis = FALSE
        finally:
            f.close()
        if newText == '':
            messagebox.showwarning(self.__class__.__name__,'ファイルを開けませんでした')
        else:
            self.textFilename = filename
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', newText)

    def menuFileSave(self):
        self.fileSave(self.textFilename, self.isSjis)
    def fileSave(self, saveFilename, saveIsSjis):
        s = self.text.get('1.0', 'end')
        if len(s) == 1:
            messagebox.showwarning(self.__class__.__name__,'保存するテキストがありません')
        return
        if saveIsSjis == TRUE:
            f = open(saveFilename, 'w')
        else:
            f = open(saveFilename, 'w', encoding='UTF-8')
        f.write(s[:-1])
        f.close()
        self.isSjis = saveIsSjis
        self.textFilename = saveFilename


    def menuFileSaveAsSjis(self):
        self.fileSaveAs(TRUE)

    def menuFileSaveAsUtf8(self):
        self.fileSaveAs(FALSE)

    def fileSaveAs(self, saveIsSjis):
        filename = filedialog.asksaveasfilename(filetypes=self.fileTypes,initialdir=self.directory,initialfile=os.path.basename(self.textFilename))
        if not filename:
            return
        self.fileSave(filename, saveIsSjis)






root = tk.Tk()
TextEdit(root)
root.mainloop()
