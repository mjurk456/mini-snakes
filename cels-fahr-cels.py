import tkinter as tk
from tkinter import ttk

def convert():
    result=0
    t="Tip: "
    absZero=t+ "at absolute zero nearly \nall molecular motion ceases."
    waterFreeze=t+"at 0°C / 32°F water freezes, \nwinter is coming :)"
    waterBoil=t+"at  100°C / 212°F water boils, \nlet's prepare a cup of tea :)"
    tipText.set(t+"\n")
    try:
        f1=float(fahrEntry.get())
    except:
        fahrToCelsText.set("Wrong value!")
        
    else:
        if f1<-459.67:
            fahrToCelsText.set("It is below absolute zero.")
            tipText.set(absZero)
        else:
            result=round((f1-32)*5/9,2)
            fahrToCelsText.set(str(result)+"°C")
        if f1==32:
            tipText.set(waterFreeze)
        elif f1==212:
            tipText.set(waterBoil)
        elif f1==-459.67:
            tipText.set(absZero)

    try:
        c1=float(celsEntry.get())
    except:
        celsToFahrText.set("Wrong value!")
    else:
        if c1<-273.15:
            celsToFahrText.set("It is below absolute zero.")
            tipText.set(absZero)
        else:
            result=round(c1*1.8+32)
            celsToFahrText.set(str(result)+"°F")
        if c1==0:
            tipText.set(waterFreeze)
        elif c1==100:
            tipText.set(waterBoil)
        elif c1==-273.15:
            tipText.set(absZero)
        
            

#main window with fixed width
main=tk.Tk()
main.title("Celsius-Fahrengeit-Celsius converter")
main.minsize(width=280, height= 130)
main.maxsize(width=280, height= 130)
main.resizable(0,0)
mainframe=ttk.Frame(main,padding="10 10 10 10",width=260, height=110)
mainframe.grid(column=0,row=0)


ttk.Label(mainframe,text="Result").grid(column=2,row=0,sticky=tk.W)

#Entry for F to C
fahrEntry=ttk.Entry(mainframe,width=6)
fahrEntry.grid(column=0,row=1,sticky=tk.W)
ttk.Label(mainframe,text="°F -> ").grid(column=1,row=1,sticky=tk.W)
fahrToCelsText=tk.StringVar()
fahrToCelsText.set("")
fahrToCelsLabel=ttk.Label(mainframe,textvariable=fahrToCelsText,width=24)
fahrToCelsLabel.grid(column=2,row=1,sticky=tk.W)

#entry for C to F
celsEntry=ttk.Entry(mainframe,width=6)
celsEntry.grid(column=0,row=2,sticky=tk.W)
ttk.Label(mainframe,text="°C -> ").grid(column=1,row=2,sticky=tk.W)
celsToFahrText=tk.StringVar()
celsToFahrText.set("")
celsToFahrLabel=ttk.Label(mainframe,textvariable=celsToFahrText,width=24)
celsToFahrLabel.grid(column=2,row=2,sticky=tk.W)

#run button
convButton=ttk.Button(mainframe,text="Convert",command=convert)
convButton.grid(row=3,columnspan=3)

#tips line
tipText=tk.StringVar()
tipText.set("Tip: \n")
tipLabel=ttk.Label(mainframe,textvariable=tipText,relief="sunken",width=32)
tipLabel.grid(row=4,columnspan=3,sticky=tk.W)
mainframe.mainloop()
