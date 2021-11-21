from tkinter import *

def B_click(numbers):
    global oper
    oper= oper+str(numbers)
    Text_Input.set(oper)

def B_clear():
    global oper
    oper= ""
    Text_Input.set("")


def B_eval():
    global oper
    rel= str(eval(oper))
    Text_Input.set(rel)

window=Tk()
Text_Input= StringVar()
oper= ""

#window
window.title("CACULACAT")
window.geometry("520x425")







entry=Entry(window,bg="light green",text=("Areal",50),bd=50,width=70,textvariable=Text_Input).grid(row=1,columnspan=4)

def quit():
    exit()

###############################################################################################
Ac=Button(window,text="AC",font=("Areal",18,"bold"),width="8",command=B_clear).grid(row=2,column=0)
Pi=Button(window,text="π",font=("Areal",18,"bold"),width="8",command =lambda :B_click("π")).grid(row=2,column=1)
On=Button(window,text="On",font=("Areal",18,"bold"),width="8").grid(row=2,column=2)
Off=Button(window,text="Off",font=("Areal",18,"bold"),width="8",command=quit).grid(row=2,column=3)
##############################################################################################
Open=Button(window,text="(",font=("Areal",18,"bold"),width="8",command =lambda :B_click("(")).grid(row=3,column=0)
Close=Button(window,text=")",font=("Areal",18,"bold"),width="8",command =lambda :B_click(")")).grid(row=3,column=1)
Percent=Button(window,text="%",font=("Areal",18,"bold"),width="8",command =lambda :B_click("%")).grid(row=3,column=2)
Divide=Button(window,text="/",font=("Areal",18,"bold"),width="8",command =lambda :B_click("/")).grid(row=3,column=3)
##############################################################################################
Seven=Button(window,text="7",font=("Areal",18,"bold"),width="8",command =lambda :B_click("7")).grid(row=4,column=0)
Eight=Button(window,text="8",font=("Areal",18,"bold"),width="8",command =lambda :B_click("8")).grid(row=4,column=1)
Nine=Button(window,text="9",font=("Areal",18,"bold"),width="8",command =lambda :B_click("9")).grid(row=4,column=2)
Times=Button(window,text="X",font=("Areal",18,"bold"),width="8",command =lambda :B_click("X")).grid(row=4,column=3)
#################################################################################################
four=Button(window,text="4",font=("Areal",18,"bold"),width="8",command =lambda :B_click("4")).grid(row=5,column=0)
five=Button(window,text="5",font=("Areal",18,"bold"),width="8",command =lambda :B_click("5")).grid(row=5,column=1)
six=Button(window,text="6",font=("Areal",18,"bold"),width="8",command =lambda :B_click("6")).grid(row=5,column=2)
minus=Button(window,text="-",font=("Areal",18,"bold"),width="8",command =lambda :B_click("-")).grid(row=5,column=3)
##############################################################################################
one=Button(window,text="1",font=("Areal",18,"bold"),width="8",command =lambda :B_click("1")).grid(row=6,column=0)
two=Button(window,text="2",font=("Areal",18,"bold"),width="8",command =lambda :B_click("2")).grid(row=6,column=1)
three=Button(window,text="3",font=("Areal",18,"bold"),width="8",command =lambda :B_click("3")).grid(row=6,column=2)
plus=Button(window,text="+",font=("Areal",18,"bold"),width="8",command =lambda :B_click("+")).grid(row=6,column=3)

###############################################################################################
dot=Button(window,text=".",font=("Areal",18,"bold"),width="8",command =lambda :B_click(".")).grid(row=7,column=0)
zero=Button(window,text="0",font=("Areal",18,"bold"),width="8",command =lambda :B_click("0")).grid(row=7,column=1)
Ans=Button(window,text="Ans",font=("Areal",18,"bold"),width="8",command =lambda :B_click("Ans")).grid(row=7,column=2)
equal=Button(window,text="=",font=("Areal",18,"bold"),width="8",command=B_eval).grid(row=7,column=3)

window.mainloop()
