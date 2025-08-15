# first window
import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("Hotel Management")
window.geometry("600x400")
window.config(bg="Teal")
tkinter.Label(text="Welcome to Hotel Management",bg="Teal",fg='black',font='Monospace 18 italic').place(x=100,y=10)

tkinter.Button(text="1.Check-Inn",font="Monospace 16").place(x=180,y=50)
tkinter.Button(text="2.Show Guest List",font="Monospace 16 ").place(x=180,y=100)
tkinter.Button(text="3.Check-out",font="Monospace 16 ").place(x=180,y=150)
tkinter.Button(text="4.Get info of any Guest",font="Monospace 16 ").place(x=180,y=200)
tkinter.Button(text="5.exit",font="Monospace 16 ").place(x=180,y=250)

window.mainloop()