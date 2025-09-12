import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Registration form")
window.geometry("700x800")
window.config(bg="Teal")

tkinter.Label(text="Firstname:",bg="Teal",fg='white',font='Monospace 18 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Last Name:",bg="Teal",fg='white',font='Monospace 18 bold').grid(row=1,column=0,sticky='w')

fnm=tkinter.Entry(font='Monospace 12 bold',)
fnm.grid(row=0,column=1,sticky='w')
lnm=tkinter.Entry(font='Monospace 12 bold',)
lnm.grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text='Male',bg='Teal',fg='Black',font='Monospace 18 bold').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text='Female',bg='Teal',fg='Black',font='Monospace 18 bold').grid(row=2,column=1,sticky='w')
tkinter.Radiobutton(value=2,text='Other',bg='Teal',fg='Black',font='Monospace 18 bold').grid(row=2,column=2,sticky='w')

tkinter.Checkbutton(text='Gujarati',bg="Teal",fg="white",font="Monospace 18 bold",).grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text='Hindi',bg="Teal",fg="white",font="Monospace 18 bold",).grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text='English',bg="Teal",fg="white",font="Monospace 18 bold",).grid(row=5,column=0,sticky='w')

city=["rajkot","Ahmedabad","Jamjodhpur","Dahod","Ratanpur","Nadiyad"]
ttk.Combobox(values=city).grid(row=6,column=0)

def btclick():
    print("firstname:-",fnm.get())
    print("Second Name:-",lnm.get())

tkinter.Button(text="Submit",font="Monospace 18 bold",command=btclick).place(x=180,y=300)

window.mainloop()