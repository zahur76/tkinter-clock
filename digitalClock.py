from tkinter import Tk, Label
import time
import sys

master = Tk()
master.title('Digital Clock')

def get_time():
    time_var = time.strftime("%H:%M:%S %p")
    clock.config(text=time_var)
    clock.after(200, get_time)
   

clock = Label(master, font=("Calibri", 30), bg="grey", fg="white")
clock.pack()
get_time()

master.mainloop()
