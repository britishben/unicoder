#unicoder_g.py - encodes a number to unicode characters
#This is the graphical version, using tkinter

from tkinter import *

def numberToBase(n,b):
    """
    Takes two decimal ints, and returns an array of ints in the desired base
    >>> numberToBase(1500,2)
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
    """

    if n == 0:
        return [0]
    digits=[]
    while n:
        digits.append( int(n%b) )
        n //= b #"floor division"
    return digits [::-1] #returns array backwards (i.e. in the right order)

def update_Text(string):
    output.delete("1.0",END)
    output.insert(END, string)
    
def runCalc():
    update_Text("--WORKING--")
    
    num=int(numberBox.get()) or 0
    base=int(baseBox.get()) or 10
    start=int(startBox.get() or "0x30", 16)

    numList=numberToBase(num,base)
    outList=""
    for i in numList:
          outList+=chr(start+i)+" "

    update_Text(outList)
    

if __name__ == '__main__':
    root = Tk()
    root.title("UniCoder")
    #root.geometry("450x150") #needs updating
   
    rowTrack=0

    numberText=Label(root, text="Number to be converted (base 10):")
    numberText.grid(row=rowTrack,sticky=E)
    numberValue = StringVar(root, value='100')
    numberBox=Entry(root, width=50, textvariable=numberValue)
    numberBox.grid(row=rowTrack+1, columnspan=2, pady=5)
    rowTrack+=2
    
    baseText=Label(root, text="Desired possible chars:")
    baseText.grid(row=rowTrack,sticky=E)
    baseValue = StringVar(root, value='10')
    baseBox=Entry(root, width=6, textvariable=baseValue)
    baseBox.grid(row=rowTrack,column=1,pady=3)
    rowTrack+=1
    
    startText=Label(root, text="Enter the unicode start point (such as 0x1400):")
    startText.grid(row=rowTrack,sticky=E)
    startValue = StringVar(root, value="0x30")
    startBox=Entry(root, width=8, textvariable=startValue)
    startBox.grid(row=rowTrack,column=1,pady=3)
    rowTrack+=1
    
    output = Text(root, height=5, width=60, bd=10)
    output.grid(row=rowTrack,columnspan=2, pady=5)
    output.insert(END,"Ready")
    rowTrack+=1
    
    button=Button(root, text="GO", command=runCalc)
    button.grid(row=rowTrack,column=0)
    exitButton=Button(root, text="quit", command=root.quit)
    exitButton.grid(row=rowTrack,column=1)
    rowTrack+=1
    
    root.mainloop()
