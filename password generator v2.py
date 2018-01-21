import tkinter as tk
from tkinter import ttk
import random as rnd

def generate_password():
    errorMsg=""
    warningMsg=""
    pswrd="" #temporary variable
    codingLine='' #temporary variable
    
    try:
        
        a=int(length.get()) #temporary variable
        if a < minPasswordLength:
            a = minPasswordLength
            warningMsg="Password is too short, its length will be set to %d symbols" \
                        % minPasswordLength
            tk.messagebox.showwarning("Warning",warningMsg)
            length.set(str(minPasswordLength))

        if a > maxPasswordLength:
            a = maxPasswordLength
            warningMsg = "Password is too long, its length will be set to %d symbols" \
                        % maxPasswordLength
            tk.messagebox.showwarning("Warning",warningMsg)
            length.set(str(maxPasswordLength))
    except ValueError:
        errorMessage="Check your password length input" 
        tk.messagebox.showerror("Error", errorMessage)
        longPasswordEntry.focus()
        return
    if (includeLetters.get()==0) and (includeCapitals.get()==0) \
            and (includeDigits.get()==0) and \
            (includeSpecSymbols.get() == 0):
        tk.messagebox.showerror("Error", \
            "Choose at least one group of symbols to create a password")
        return
    if includeSpecSymbols.get() and (specSymbols.get()==""):
        errorMessage="Input special symbols to be used" 
        tk.messagebox.showerror("Error", errorMessage)
        specSymbolsEntry.focus()
        return
# ************ MNEMONIC 
    if strength.get()==0:
        if includeDigits.get():
            pswrd=pswrd + \
                   "".join(str(x) for x in \
                           rnd.sample(range(0,10),2))
            codingLine = codingLine + "0123456789"
        if includeSpecSymbols.get():
            pswrd = rnd.choice(specSymbols.get()) + pswrd
            codingLine = codingLine + specSymbols.get()
        if includeCapitals.get():
            pswrd = rnd.choice(vowels.upper()) + pswrd
            codingLine = codingLine + vowels.upper() \
                         + consonants.upper()
        if includeLetters.get():
            
            if ((a - len(pswrd)) % 2) == 1:
                if pswrd[0] in vowels.upper():
                    pswrd = pswrd[0] + rnd.choice(consonants) \
                            + pswrd[1:]
                else:
                    pswrd = rnd.choice(consonants) + pswrd
            for i in range(0, a-len(pswrd), 2):
                try:
                    if pswrd[0] in vowels.upper():
                       pswrd = pswrd[0] + rnd.choice(consonants) \
                            + rnd.choice(vowels) + pswrd[1:]
                    else:
                        pswrd = rnd.choice(consonants) + \
                            rnd.choice(vowels) + pswrd
                except IndexError:
                    pswrd = rnd.choice(consonants) + \
                            rnd.choice(vowels) + pswrd
        else:
            if includeCapitals.get():
                if (a - len(pswrd)) % 2 == 1:
                    pswrd = pswrd + rnd.choice(consonants.upper())
                for i in range(0,a-len(pswrd),2):
                    pswrd = pswrd + rnd.choice(consonants.upper()) \
                        + rnd.choice(vowels.upper())
            else:
                if len(codingLine) < a:
                    codingLine = codingLine * 28
                rndList = rnd.sample(range(len(codingLine)),a)
                for i in range(a-len(pswrd)):
                    pswrd=pswrd+codingLine[rndList[i]]
# random symbols
    elif strength.get() == 1:
        if includeLetters.get():
            codingLine = codingLine+vowels+consonants
            pswrd = pswrd + rnd.choice(vowels+consonants)
        if includeCapitals.get():
            codingLine = codingLine + vowels.upper() + \
                        consonants.upper()
            pswrd = pswrd + rnd.choice(vowels.upper() \
                        + consonants.upper())
        if includeDigits.get():
            codingLine = codingLine + "0123456789"
            pswrd = pswrd + str(rnd.randint(0,9))
        if includeSpecSymbols.get():
            codingLine = codingLine + specSymbols.get()
            pswrd = pswrd + rnd.choice(specSymbols.get())
        if len(codingLine) < a:
            codingLine = codingLine * 28
        rndList = rnd.sample(range(len(codingLine)),a)
        
        for i in range(a-len(pswrd)):
            pswrd=pswrd+codingLine[rndList[i]]
    genPassword.set(pswrd)

def copy_to_clipboard():
    main.clipboard_append(genPassword.get())
    
main=tk.Tk()
main.title("Password Generator")
mainframe=ttk.Frame(main,padding="10 10 10 10")
mainframe.grid(column=0,row=0)

#declarations
specSymbols=tk.StringVar()
specSymbols.set("-_!+")
includeLetters=tk.IntVar()
includeLetters.set(1) #including letters by default
includeCapitals=tk.IntVar()
includeDigits=tk.IntVar()
includeSpecSymbols=tk.IntVar()
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxz"
maxPasswordLength=28
minPasswordLength=6

#password type
ttk.Label(mainframe,text="Select password type:").grid(columnspan=2, \
                row=0,sticky=tk.W)
strength=tk.IntVar()
ttk.Radiobutton(mainframe,text="Mnemonic (easy to remember)", \
                variable=strength,value=0).grid(columnspan=2,row=1,sticky=tk.W)
ttk.Radiobutton(mainframe,text="Random symbols (difficult to remember)", \
                variable=strength,value=1).grid(columnspan=2,row=2,sticky=tk.W)

#symbols to include
symbolFrame=ttk.Frame(mainframe,padding="0 10 0 0")
symbolFrame.grid(columnspan=2,row=3,sticky=tk.W)
ttk.Label(symbolFrame,text="Select symbols to include:").grid(columnspan=2, \
                row=0, sticky=tk.W)

ttk.Checkbutton(symbolFrame,text="Letters a-z",variable=includeLetters) \
                .grid(columnspan=2,row=1,sticky=tk.W)
ttk.Checkbutton(symbolFrame,text="Capital letters A-Z",variable=includeCapitals) \
                .grid(columnspan=2,row=2,sticky=tk.W)
ttk.Checkbutton(symbolFrame,text="Digits 0-9",variable=includeDigits) \
                .grid(columnspan=2,row=3,sticky=tk.W)
ttk.Checkbutton(symbolFrame,text="Special symbols ",variable=includeSpecSymbols) \
                .grid(column=0,row=4,sticky=tk.W)
specSymbolsEntry = ttk.Entry(symbolFrame,width=6,textvariable=specSymbols)
specSymbolsEntry.grid(column=1,row=4,sticky=tk.W)

#password length
ttk.Label(mainframe,text="Select a password length (%d-%d symbols): " % \
                (minPasswordLength, maxPasswordLength)) \
                .grid(column=0,row=8,pady=(10,0),sticky=tk.W+tk.S)
length=tk.StringVar()
length.set("8")
longPasswordEntry=ttk.Entry(mainframe,width=6,textvariable=length)
longPasswordEntry.grid(column=1,row=8,pady=(10,0), sticky=tk.W+tk.S)
ttk.Label(mainframe,text="Generated password").grid( \
    columnspan=2,row=11,pady=10)
genPassword=tk.StringVar()
genPassword.set("")
genPasswordEntry=ttk.Entry(mainframe,width=40,textvariable=genPassword)
genPasswordEntry.grid(columnspan=2,row=12,sticky=tk.W)

buttonframe=ttk.Frame(mainframe, padding="10 10 10 10")
buttonframe.grid(columnspan=2,row=13)
genPasswordButton=ttk.Button(buttonframe,text="Generate",command=generate_password)
genPasswordButton.grid(row=0,column=0, sticky=tk.E,pady=5)
copyButton=ttk.Button(buttonframe,text="Copy to clipboard",command=copy_to_clipboard)
copyButton.grid(row=0,column=1,sticky=tk.W,padx=5)
main.mainloop()
