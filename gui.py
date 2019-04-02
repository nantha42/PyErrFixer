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
    print(f.name)
    global filename
    filename = f.name.split('/')[-1]

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
    t = p.getreport()
    lines= p.send_string(lines)

    text.delete(0.0,END)
    text.insert(0.0,lines)

def run():

    str = entry.get()
    items = str.split('/')
    str = str[:-3]
    path = "/"
    for i in range(len(items)-1):
        path+= items[i]+'/'
    sys.path.insert(0,path)
    print(str)
    p = Process(items[-1][:-3],path)
    print(p.getreport())
    text.delete(0.0,END)
    text.insert(0.0,p.getreport())

def callprocess():

    print("called")
    print(str)


root = Tk()
root.title("Indent Corrector")
root.minsize(width=300,height=300)
root.minsize(width=300,height=300)

"""
editor = Frame(root,width=600,height=500)
editor.place(x=0,y=0)
console = Frame(root,width=600,height=200)
console.place(x=0,y=530)

text = Text(editor)
text.place(x=0,y=0,width=600,height=500)
labelo = Label(text="output:");
labelo.place(x=0,y=500)

output = Text(console)
output.place(x=0,y=0,width=600,height=150)
"""

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

runmenu = Menu(menubar)
runmenu.add_command(label="Run",command=run)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
menubar.add_cascade(label="Run",menu=runmenu)


editor = Frame(root,width=300,height=200)
editor.grid(row=2,column=1)
text = Text(editor)
text.place(x=0,y=0,width=300,height=200)
#labelo = Label(text="output:");
#labelo.place(x=0,y=500)

label = Label(root,text="Filepath")
label.grid(row= 1,column=1)
entry = Entry(root)
entry.grid(row=1,column=2)

#entry.bind('<Return>',callprocess)
root.config(menu=menubar)
root.mainloop()