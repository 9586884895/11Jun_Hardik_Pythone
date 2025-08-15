import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Hotel Management system")
window.geometry("600x400")
window.config(bg="Teal")

tkinter.Label(text="Enter your Name:  ",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=0,column=0,sticky="w")
tkinter.Label(text="Enter your address:  ",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=1,column=0,sticky="w")
tkinter.Label(text="Enter Your Number:  ",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=2,column=0,sticky="w")
tkinter.Label(text="Enter Your Days:  ",bg="Teal",fg='white',font='Monospace 14 bold').grid(row=3,column=0,sticky="w")

nm=tkinter.Entry(font='Monospace 12 bold',)
nm.grid(row=0,column=1,sticky="w")
cn=tkinter.Entry(font='Monospace 12 bold',)
cn.grid(row=1,column=1,sticky="w")
ml=tkinter.Entry(font='Monospace 12 bold',)
ml.grid(row=2,column=1,sticky="w")
dy=tkinter.Entry(font='Monospace 12 bold',)
dy.grid(row=3,column=1,sticky="w")
tkinter.Label(text="Choose your Room:",bg="Teal",fg='white',font='Monospace 14 bold').place(x=0,y=120)
tkinter.Checkbutton(text='Deluxe',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=4,column=2,sticky='w')
tkinter.Checkbutton(text='Full Deluxe',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=5,column=2,sticky='w')
tkinter.Checkbutton(text='General',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=4,column=1,sticky='w')
tkinter.Checkbutton(text='Joint',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=5,column=1,sticky='w')

tkinter.Label(text="Payment Method:",bg="Teal",fg='white',font='Monospace 14 bold').place(x=0,y=180)
tkinter.Checkbutton(text='By cash',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=6,column=1,sticky='w')
tkinter.Checkbutton(text='By card',bg="Teal",fg="black",font="Monospace 14 bold",).grid(row=6,column=2,sticky='w')

tkinter.Button(text="Submit",font="Monospace 18 bold").place(x=250,y=250)


window.mainloop()