from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as tkscrolled

root = Tk()
root.title("Steming")
root.geometry("1160x600")
root.resizable(0,0)

def showOriginalText():
    pass

def showStopWords():
    pass

def showUniqueWords():
    pass

def showInfix():
    pass

def showPrefix():
    pass

def showPostfix():
    pass

def customization():
    pass


def showPostProcessing():
    pass

tabbuttons = Frame(root)
b1 = Button(tabbuttons,text="Original Text", command=showOriginalText, height=1, width=20)
b1.grid(row=1, column=0)
b2 = Button(tabbuttons,text="Stop Words", command=showStopWords, height=1, width=20)
b2.grid(row=1, column=1)
b3 = Button(tabbuttons,text="Unique Words", command=showUniqueWords, height=1, width=20)
b3.grid(row=1, column=2)
b4 = Button(tabbuttons,text="Prefix", command=showPrefix, height=1, width=20)
b4.grid(row=1, column=3)
b5 = Button(tabbuttons,text="Postfix", command=showPostfix, height=1, width=20)
b5.grid(row=1, column=4)
b6 = Button(tabbuttons,text="Post-Processing", command=showPostProcessing, height=1, width=20)
b6.grid(row=1, column=5)
b7 = Button(tabbuttons,text="Infix", command=showInfix, height=1, width=20)
b7.grid(row=1, column=6)
tabbuttons.grid(row=1, pady=(30,0))

textbox = tkscrolled.ScrolledText(root, height=20, width=132)
textbox.grid(row=2, pady=(0,20), padx=50)

def InputFile():                                                                            # Function For Browsing File
    root.filename = filedialog.askopenfilename(title = "Select File", filetypes = [('Text files', '*.txt')])
    f = open(root.filename,encoding="utf8")
    content = f.read()
    # data = str(content)
    print(type(content))
    textbox.insert(INSERT,content)
   # print(content)
   # data = content.split("۔")

def stemData():
    pass

buttons = Frame(root)                                                                                  # Three Main Buttons Frame
clear = Button(buttons, text= "Clear" , command= lambda: textbox.delete(1.0,END), height=2, width=20)   # Clear Button
browsebutton = Button(buttons, text ="Browse From Computer",command = InputFile, height=2)              # Browse Button
browsebutton.grid(row=3,column=1, padx=4)
clear.grid(row=3,column=2, padx=4)
buttons.grid()
submitButton = Button(root, text="Stemming", command= stemData, width= 20, height= 2, bg = "yellow", font='bold')                  # Submit Button
submitButton.config(font=("Calibri", 15))
submitButton.grid(pady=(20,15))
root.mainloop()

