from tkinter import *
from tkinter import ttk

#this is the function that does the conversion
def calculate():
    try:
        value = float(meter.get())
        Centimeter.set(0.39*value)
    except ValueError:
        print("Sorry, that's not a valid number. Try again")


win = Tk()
win.title("Centimeters to Inches")

#create the frame
window = ttk.Frame(win)
window.grid(column=0, row=0)

meter = StringVar()
meter_entry = ttk.Entry(window, width=7, textvariable=meter)
meter_entry.grid(column=2, row=1)

#create labels
ttk.Label(window, text='centimeter').grid(column=3, row=1)
ttk.Label(window, text='is equivalent to').grid(column=1, row=2)
ttk.Label(window, text='inches').grid(column=3, row=2)

#create label and button
Centimeter = StringVar()
ttk.Label(window, textvariable=Centimeter).grid(column=2, row=2)
ttk.Button(window, text="calculate", command=calculate).grid(column=3, row=3)

#create space between the labels
for child in window.winfo_children():
    child.grid_configure(padx=4, pady=3)




win.mainloop()
