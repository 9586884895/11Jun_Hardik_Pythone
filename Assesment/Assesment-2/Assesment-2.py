#second window

import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Registration form")
window.geometry("500x600")
window.config(bg="Teal")
tkinter.Label(text="Please enter Details Below",bg="pink",fg='black',font='Monospace 14 bold').grid(row=0,column=1,sticky="n")
tkinter.Label(text="Name*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=2,column=0,sticky="n")
tkinter.Label(text="Contact*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=3,column=0,sticky="n")
tkinter.Label(text="Email*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=4,column=0,sticky="n")

nm=tkinter.Entry(font='Monospace 12 bold',)
nm.grid(row=2,column=1,sticky="w")
cn=tkinter.Entry(font='Monospace 12 bold',)
cn.grid(row=3,column=1,sticky="w")
ml=tkinter.Entry(font='Monospace 12 bold',)
ml.grid(row=4,column=1,sticky="w")

tkinter.Label(text="Gender*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=5,column=0,sticky="n")
tkinter.Radiobutton(value=0,text='Male',bg='Teal',fg='Black',font='Monospace 14 bold').grid(row=5,column=1,sticky='w')
tkinter.Radiobutton(value=1,text='Female',bg='Teal',fg='Black',font='Monospace 14 bold').grid(row=5,column=1,sticky='n')

tkinter.Label(text="City*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=6,column=0,sticky="n")
tkinter.Label(text="State*",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=7,column=0,sticky="n")

city=["rajkot","Ahmedabad","Jamjodhpur","Dahod","Ratanpur","Nadiyad"]
ttk.Combobox(values=city).grid(row=6,column=1,sticky='w')

state=["Gujarat","Madhya pradesh","Rajashthan","Maharashtra","odisha","Telangana"]
ttk.Combobox(values=state).grid(row=7,column=1,sticky='w')
tkinter.Button(text="Submit",font="Monospace 14 bold").place(x=180,y=220)
window.mainloop()