from tkinter import *


class VisualiserUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Sorting Algorithm Visualiser")
        self.window.config(bg="light gray", width=900, height=600)
        self.window.resizable(width=False, height=False)
        self.window.minsize(width=900, height=600)
        self.list_size_bar = Scale(orient=HORIZONTAL)
        self.list_size_bar.config(resolution=5, from_=0, to=50)
        self.list_size_bar.grid(row=0, column=1)

        self.window.mainloop()
