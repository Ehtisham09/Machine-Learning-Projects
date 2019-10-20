from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as tkscrolled

from sumy.nlp.UrduParser import split_text
from sumy.parsers.plaintext import PlaintextParser, customtokenize
from sumy.nlp.tokenizers import Tokenizer, UrduTokenizer
from postagging import postagger
from postagging.postagger import applyPosTagging
from stemming.src import MyUrdStemming
from stemming.src.UrduDocumentStemmer import urdustemmer

sentences = []
v = IntVar
root = Tk()
root.title("Extractive Text Summarization")
root.geometry("850x560")

label0 = Label(root, text="Input Text: ", )
label0.config(font=("Calibri", 15))
label0.grid(row=1, column=0,pady=(20,0),padx=100, sticky= "nw")
textbox = tkscrolled.ScrolledText(root, height=10, width=80)
textbox.grid(row=2, pady=(0,20), padx=100)

def InputFile():                                                                            # Function For Browsing File
    root.filename = filedialog.askopenfilename(title = "Select File", filetypes = [('Text files', '*.txt')])
    f = open(root.filename,encoding="utf8")
    content = f.read()
    # data = str(content)
    textbox.insert(INSERT,content)
   # print(content)
    data = content.split("۔")
    # data = content.split(".")
    for x in data:
        sentences.append(x)

def insertCursor():
    textbox.mark_set(INSERT,"%d.%d" % (1,0))

buttons = Frame(root)                                                                                  # Three Main Buttons Frame
clear = Button(buttons, text= "Clear" , command= lambda: textbox.delete(1.0,END), height=2, width=20)   # Clear Button
browsebutton = Button(buttons, text ="Browse From Computer",command = InputFile, height=2)              # Browse Button
browsebutton.grid(row=3,column=1, padx=4)
clear.grid(row=3,column=2, padx=4)
buttons.grid()

threshold = Scale(root, from_=0, to=40, orient=HORIZONTAL, length=600, width=25, activebackground = "yellow", tickinterval=3, command= "#")                 # Horizontal Scroll Bar
threshold.grid(pady=10)
label1 = Label(root, text= "Scroll to the number of lines you want to Summarize")                  # Label Under Scroll Bar
label1.config(font=("Calibri", 15))
label1.grid()


def getScaleVal():                                                                                                 # Function To Check Scroll Bar value and Submit Button

    tt = textbox.get(1.0,END)
    if (len(sentences)==0 and len(tt) == 1):
        messagebox.showerror("No Input", "Please Enter Some Text First")

    # if (len(sentences)==0 and len(tt)>1):
    #     data = content.split("۔")
    #     for x in entrytext:
    #         sentences.append(x)

    if (threshold.get()>0 and threshold.get()<= len(sentences)):
        print(threshold.get())
        for x in range(threshold.get()):
            print(sentences[x])
        textbox.delete(1.0, END)
        sentences.clear()
        messagebox.showinfo("Bingo","Your text has been Summarized")

    elif(threshold.get() > len(sentences) and len(sentences) > 0):
        messagebox.showerror("Out Of Bounds", "Please Select a Legitimate Number")
        sentences.clear()

    print(var.get())
    print(var2.get())
    var.set("Tokenization")
    var2.set("Algorithms")
    var3.set("Evaluation")


def tokens(value):
    print(value)
    var.set("Tokenization")
    if value=='One' or value=='Two':
        tokens=customtokenize(textbox.get("1.0",END))
        sent=split_text(textbox.get("1.0",END))

        messagebox.showinfo("Token Statistics", "Total Number of Setences="+" "+str(len(sent))+"\n"+"Total Number of Tokens="+" "+str(len(tokens))+"\n"+str(tokens))


def selectAlgo(value):
    print(value)
    var2.set("Algorithms")
    if value=='Gensim':
        print()
    elif value=='LSA':
        print()

    elif value=='LUHN':
        print()

    elif value=='LEX':
        print()
    elif value == 'PyTeaser':
        print()


def evaluate(value):
    print(value)
    var3.set("Evaulation")
    if value=='Rouge Score':
        print()
    elif value=='Bleu Score':
        print()


def steming():
    pass
    text = textbox.get("1.0", END)
    text = "".join(text)
    actualTokens=len(customtokenize(text))
    res =urdustemmer(text)
    messagebox.showinfo("Stemmed Text", "Total Number of Tokens Before Stemming=" + " " + str(actualTokens) + "\n"
                        + "Total Number of Tokens After Stemming=" + " " + str(len(res)) + "\n"
                        + str(res))


def StopWardRemoval():
    pass

    text = textbox.get("1.0", END)
    text = "".join(text)
    actualTokens = len(customtokenize(text))
    # res = removeStopWords(text)
    # messagebox.showinfo("Stop Words Removal", "Total Number of Tokens Before Stop Words Removal=" + " " + str(actualTokens) + "\n"
    #                     + "Total Number of Tokens After Stop Words Removal=" + " " + str(len(res)) + "\n"
    #                     + str(res))


def POSTag():
    pass
    text=textbox.get("1.0",END)
    text="".join(text)
    res=applyPosTagging(text)
    messagebox.showinfo("POS TAGGING","Total Number of Documents=" + " " + "1" + "\n"  + str(res))








ddmFrame = Frame(root, width = 100, height=15)
ddmFrame.grid(row=10, pady=10)
var = StringVar(ddmFrame)
var.set("Tokenization")
drop1 = OptionMenu(ddmFrame, var, "One", "Two", command=tokens)
drop1.config(height= 1,width=10)
drop1.grid(row = 10,column=0,padx=3,pady=3)
button2 = Button(ddmFrame, text = "Stemming", command = steming ,height= 1, width=10)
button2.grid(row=10,column=1,padx=3,pady=3)
button3= Button(ddmFrame, text="Stop Words Removal", command=StopWardRemoval)
button3.grid(row=10,column=2,padx=3,pady=3)
button4 = Button(ddmFrame, text="POS Tagging", command=POSTag, width=10)
button4.grid(row=10,column=3, padx=3,pady=3)
var2 = StringVar(ddmFrame)
var2.set("Algorithms")
drop2 = OptionMenu(ddmFrame, var2, "Gensim", "LSA", "LUHN", "LEX","PyTeaser", command=selectAlgo)
drop2.config(width = 10)
drop2.grid(row=10, column=4,padx=5,pady=5)
var3 = StringVar(ddmFrame)
var3.set("Evaluation")
drop3 = OptionMenu(ddmFrame, var3, "Rouge Score", "Bleu Score", command=evaluate)
drop3.config(width=10)
drop3.grid(row=10,column=5,padx=3,pady=3)


submitButton = Button(root, text="Summarize", command= getScaleVal, width= 20, height= 2, bg = "yellow", font='bold')                  # Submit Button
submitButton.config(font=("Calibri", 15))
submitButton.grid(pady=15)

root.mainloop()
