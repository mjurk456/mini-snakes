import tkinter as tk
from tkinter import ttk
import random as rnd

def generate_password():
    letters="qwertyuiopasdfghjklzxcvbnm"
    specials="=_*+.#@%&"
    pswrd="" #temporary variable
    try:
        a=int(length.get()) #temporary varable
        if a<5:
            a=5
            errorLengthLabelText.set("Wrong length, a password will be 5 symbols long")
        elif a>26:
            errorLengthLabelText.set("Wrong length, a password will be 26 symbols long")
            a=26
        else:
            errorLengthLabelText.set("")
    except:
        errorLengthLabelText.set("Wrong length, a password will be 8 symbols long")
        length.set("8")
        a=8
    if strength.get()==0:
        for i in range(a):
            pswrd=pswrd+letters[i]
    elif strength.get()==1:
        for i in range(a-3):
            pswrd=pswrd+letters[rnd.randrange(len(letters))]
        for i in range(3):
            pswrd=pswrd+str(rnd.randrange(0,9))
    elif strength.get()==2:
        for i in range(a):
            #to receive more "normal" frequency of symbols
            symbChoice=rnd.randrange(1,10)
            if symbChoice in range(3):
                pswrd=pswrd+letters[rnd.randrange(len(letters))].upper()
            elif symbChoice in range(3,7):
                pswrd=pswrd+letters[rnd.randrange(len(letters))]
            elif symbChoice in range(7,9):
                pswrd=pswrd+str(rnd.randrange(0,9))
            elif symbChoice in range(9,11):
                pswrd=pswrd+specials[rnd.randrange(len(specials))]
    genPassword.set(pswrd)

def copy_to_clipboard():
    main.clipboard_append(genPassword.get())
    
main=tk.Tk()
main.title("Password Generator")
mainframe=ttk.Frame(main,padding="10 10 10 10")
mainframe.grid(column=0,row=0)
#password strength
ttk.Label(mainframe,text="Select a password strength").grid(columnspan=2,row=0,sticky=tk.W)
strength=tk.IntVar()
ttk.Radiobutton(mainframe,text="Weak (only letters)",variable=strength,value=0).grid(columnspan=2,row=1,sticky=tk.W)
ttk.Radiobutton(mainframe,text="Normal (letters and digits)",variable=strength,value=1).grid(columnspan=2,row=2,sticky=tk.W)
ttk.Radiobutton(mainframe,text="Strong (letters, digits and special symbols)",variable=strength,value=2).grid(columnspan=2,row=3,sticky=tk.W)

#password length
ttk.Label(mainframe,text="Select a password length (5-26 symbols): ").grid(column=0,row=4,sticky=tk.W)
length=tk.StringVar()
length.set("8")
longPasswordEntry=ttk.Entry(mainframe,width=6,textvariable=length)
longPasswordEntry.grid(column=1,row=4,sticky=tk.W)
errorLengthLabelText=tk.StringVar()
errorLengthLabelText.set("")
errorLabel=ttk.Label(mainframe,text="",textvariable=errorLengthLabelText)
errorLabel.grid(row=5,columnspan=2)
errorLabel.config(foreground="red")


ttk.Label(mainframe,text="Generated password").grid( \
    columnspan=2,row=6,pady=10)
genPassword=tk.StringVar()
genPassword.set("")
genPasswordEntry=ttk.Entry(mainframe,width=40,textvariable=genPassword)
genPasswordEntry.grid(columnspan=2,row=7,sticky=tk.W)

buttonframe=ttk.Frame(mainframe, padding="10 10 10 10")
buttonframe.grid(columnspan=2,row=8)
genPasswordButton=ttk.Button(buttonframe,text="Generate",command=generate_password)
genPasswordButton.grid(row=0,column=0, sticky=tk.E,pady=5)
copyButton=ttk.Button(buttonframe,text="Copy to clipboard",command=copy_to_clipboard)
copyButton.grid(row=0,column=1,sticky=tk.W,padx=5)
main.mainloop()
