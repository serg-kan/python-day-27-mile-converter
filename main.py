# import tkinter
from tkinter import *

window = Tk()
window.title("Mile converter")
window.minsize(width=500, height=300)

def button_click(entry_name):
    my_label["text"] = entry_name.get()
    print("I got clicked")

# Label
my_label = Label(text="Mile converter", font=("Arial", 24, "bold"))
# my_label.pack()

# Entry
input = Entry(width=10)
# input.pack()
# input.get()

# Button
button = Button(text="Click Me", command=lambda: button_click(input))
# button.pack()
new_button = Button(text="Second button")

my_label.grid(row=1, column=1)
button.grid(row=2, column=2)
new_button.grid(row=1, column=3)
input.grid(row=3, column=4)

window.mainloop()
