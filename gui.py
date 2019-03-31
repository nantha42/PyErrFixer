from tkinter import *
from main import Process
from tkinter.filedialog import *;
import os

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)

def saveFile():
    global filename
    t = text.get(0.0,END)
    f = open(filename,"w")
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode="w",defaultextension='.txt')
    t = text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        print("error")

def openFile():
    f = askopenfile(mode="r")
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

def indent():
    lines = text.get(0.0,END)
    p = Process()
    lines= p.send_string(lines)
    text.delete(0.0,END)
    text.insert(0.0,lines)

root = Tk();
root.title("Text Editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save as..",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="QUit",command=root.quit)

editmenu = Menu(menubar)
editmenu.add_command(label="Indent",command=indent)


menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)

root.config(menu=menubar)
root.mainloop()