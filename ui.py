from tkinter import *

window = Tk()
window.title("Sorting Algorithm Visualiser")
window.config(bg="light gray", width=900, height=600)
window.resizable(width=False, height=False)
window.minsize(width=900, height=600)

list_size_bar = Scale(orient=HORIZONTAL)
list_size_bar.config(resolution=5, from_=0, to=50)
list_size_bar.grid(row=0,column=1)




window.mainloop()
