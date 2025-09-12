import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Calculator")
window.geometry("500x500")
window.config(bg="Teal")


tkinter.Label(text="First Value:",bg="Teal",fg='white',font='Monospace 18 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Last Value:",bg="Teal",fg='white',font='Monospace 18 bold').grid(row=1,column=0,sticky='w')

fvl=tkinter.Entry(font='Monospace 12 bold',)
fvl.grid(row=0,column=1,sticky='w')
lvl=tkinter.Entry(font='Monospace 12 bold',)
lvl.grid(row=1,column=1,sticky='w')

def Multiplication():
    '''print("first Value:-",fvl.get())
    print("Second Value:-",lvl.get())
    print("Multiplication:- ",int(fvl.get())*int(lvl.get()))
    '''
    result = int(fvl.get())*int(lvl.get())
    print("Multiplication is : ",result)
    rslbl.config(text=f"Final Answer:-: {result}")
0
def Sum():
    result = int(fvl.get())+int(lvl.get())
    print("Sum is : ",result)
    rslbl.config(text=f"Final Answer:-: {result}")
    
def Minus():
    result = int(fvl.get())-int(lvl.get())
    print("Substraction is : ",result)
    rslbl.config(text=f"Final Answer:-: {result}")
    
def Divide():
    result = int(fvl.get())/int(lvl.get())
    print("Multiplication is : ",result)
    rslbl.config(text=f"Final Answer:-: {result}")

tkinter.Button(text="MUL",font="Monospace 18 bold",command=Multiplication).place(x=20,y=80)
tkinter.Button(text="SUM",font="Monospace 18 bold",command=Sum).place(x=100,y=80)
tkinter.Button(text="SUB",font="Monospace 18 bold",command=Minus).place(x=180,y=80)
tkinter.Button(text="DIV",font="Monospace 18 bold",command=Divide).place(x=260,y=80)

rslbl=tkinter.Label(text="Final Answer :-",bg="Black",fg='white',font='Monospace 18 bold')
rslbl.place(x=50,y=150)



window.mainloop()
