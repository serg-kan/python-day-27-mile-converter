# import tkinter
from tkinter import *

window = Tk()
window.title("Mile converter")
window['padx'] = 20
window['pady'] = 20

def button_click(entry_name):
    label_result["text"] = round((int(entry_name.get()) * 1.60934), 2)
    print("I got clicked")

# Layout
input_mile = Entry(width=10)
label_mile = Label(text="Mile converter")
label_is_equal = Label(text="is equal to")
label_result = Label(text="")
label_km = Label(text="Km")

button = Button(text="Calculate", command=lambda: button_click(input_mile))


input_mile.grid(row=1, column=2)
label_mile.grid(row=1, column=3)
label_is_equal.grid(row=2, column=1)
label_result.grid(row=2, column=2)
label_km.grid(row=2, column=3)
button.grid(row=3, column=2)

window.mainloop()
