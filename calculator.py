from tkinter import *   
from tkinter import messagebox
top = Tk()  
top.geometry("310x440")  
top.title('Calculator')
top.configure(bg='#696969')

def btn_click(item):
    global exp
    exp=exp+str(item)
    txt.set(exp)
def clear():
    global exp
    exp=""
    txt.set(exp)
def equal():
    global exp
    if(exp==""):
        txt.set("Invalid expression!")   
    result=str(eval(exp))
    txt.set(result)
    exp=""

exp=""
txt=StringVar()

e1=Entry(top,textvariable=txt,width=46,bg='#424242',fg='white').grid(row=0,column=0,columnspan=4,pady=30,padx=7,ipady=15)

b1=Button(top,text='1',height=3,width=7,command=lambda: btn_click(1),fg='white',bg='#424242').grid(row=1,column=0,pady=6,padx=7)
b1=Button(top,text='2',height=3,width=7,command=lambda: btn_click(2),fg='white',bg='#424242').grid(row=1,column=1,pady=6,padx=7)
b1=Button(top,text='3',height=3,width=7,command=lambda: btn_click(3),fg='white',bg='#424242').grid(row=1,column=2,pady=6,padx=7)
b1=Button(top,text='C',height=3,width=7,command=clear,fg='white',bg='brown').grid(row=1,column=3,pady=6,padx=7)

b1=Button(top,text='4',height=3,width=7,command=lambda: btn_click(4),fg='white',bg='#424242').grid(row=2,column=0,pady=6,padx=7)
b1=Button(top,text='5',height=3,width=7,command=lambda: btn_click(5),fg='white',bg='#424242').grid(row=2,column=1,pady=6,padx=7)
b1=Button(top,text='6',height=3,width=7,command=lambda: btn_click(6),fg='white',bg='#424242').grid(row=2,column=2,pady=6,padx=7)
b1=Button(top,text='*',height=3,width=7,command=lambda: btn_click('*'),fg='white',bg='#424242').grid(row=2,column=3,pady=6,padx=7)

b1=Button(top,text='7',height=3,width=7,command=lambda: btn_click(7),fg='white',bg='#424242').grid(row=3,column=0,pady=6,padx=7)
b1=Button(top,text='8',height=3,width=7,command=lambda: btn_click(8),fg='white',bg='#424242').grid(row=3,column=1,pady=6,padx=7)
b1=Button(top,text='9',height=3,width=7,command=lambda: btn_click(9),fg='white',bg='#424242').grid(row=3,column=2,pady=6,padx=7)
b1=Button(top,text='/',height=3,width=7,command=lambda: btn_click('/'),fg='white',bg='#424242').grid(row=3,column=3,pady=6,padx=7)

b1=Button(top,text='0',height=3,width=7,command=lambda: btn_click(0),fg='white',bg='#424242').grid(row=4,column=0,pady=6,padx=7)
b1=Button(top,text='.',height=3,width=7,command=lambda: btn_click('.'),fg='white',bg='#424242').grid(row=4,column=1,pady=6,padx=7)
b1=Button(top,text='+',height=3,width=7,command=lambda: btn_click('+'),fg='white',bg='#424242').grid(row=4,column=2,pady=6,padx=7)
b1=Button(top,text='-',height=3,width=7,command=lambda: btn_click('-'),fg='white',bg='#424242').grid(row=4,column=3,pady=6,padx=7)

b1=Button(top,text='=',height=2,width=40,command=equal,fg='white',bg='#52528B').grid(row=5,column=0,columnspan=4,pady=6,padx=7)

top.mainloop()