import tkinter.ttk
from algorthms import get_random_list
from tkinter import *


class VisualiserUI:

    def __init__(self):
        # ------------ root --------------#
        self.window = Tk()
        self.window.title("Sorting Algorithm Visualiser")
        self.window.config(bg="black")
        self.window.resizable(width=False, height=False)
        self.window.maxsize(width=900, height=600)

        # ------------ Frame --------------#
        self.frame = Frame(master=self.window, width=900, height=200, bg="grey")
        self.frame.grid(row=0, column=0, padx=5, pady=5,)

        # ------------ Canvas --------------#
        self.canvas = Canvas(master=self.window, width=900, height=400, bg="white")
        self.canvas.grid(row=1, column=0, padx=5, pady=5)

        # ------------ Scale --------------#
        self.list_size_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.list_size_scale.config(resolution=1, from_=2, to=50, label="Array Size")
        self.list_size_scale.grid(row=1, column=0, padx=20, pady=5)

        self.min_value_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.min_value_scale.config(resolution=1, from_=0, to=10, label="Min Value")
        self.min_value_scale.grid(row=1, column=1, padx=20, pady=5)

        self.max_value_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.max_value_scale.config(resolution=1, from_=10, to=100, label="Max Value")
        self.max_value_scale.grid(row=1, column=2, padx=20, pady=5)

        self.sort_speed_scale = Scale(master=self.frame, orient=HORIZONTAL, length=200)
        self.sort_speed_scale.config(resolution=0.1, from_=0.1, to=2, label="Select Speed [s]")
        self.sort_speed_scale.grid(row=0, column=2, padx=20, pady=5)

        # ------------ Buttons --------------#
        self.generate_button = Button(master=self.frame, text="Generate Array", command=self.generate_array)
        self.generate_button.grid(row=1, column=3)

        self.run_algorithm_button = Button(master=self.frame, text="Run algorith", command=self.run_algorithm)
        self.run_algorithm_button.grid(row=0, column=3)

        # ------------ Labels --------------#
        self.algorithm_value = tkinter.StringVar()

        self.algorithm_label = Label(master=self.frame, text="Algorithm: ", bg="gray")
        self.algorithm_label.grid(row=0, column=0, padx=5, pady=5)

        self.algorithm_menu = tkinter.ttk.Combobox(master=self.frame,
                                                   textvariable=self.algorithm_value,
                                                   values=["Bubble Sort", "Merge Sort"])
        self.algorithm_menu.grid(row=0, column=1,padx=5, pady=5)
        self.algorithm_menu.current(0)

        self.window.mainloop()

    def generate_array(self):
        self.canvas.delete("all")
        random_list = get_random_list(list_size=self.list_size_scale.get(),
                                      min_value=self.min_value_scale.get(),
                                      max_value=self.max_value_scale.get())

        offset = 30
        c_width = 900 - (offset / 2)
        c_height = 400
        spacing = 5
        x_width = c_width / self.list_size_scale.get()

        normalised_data = [i / max(random_list) for i in random_list]

        for i, array_height in enumerate(normalised_data):
            x0 = i * x_width + spacing
            y0 = c_height - array_height * 370
            x1 = (i + 1) * x_width
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            self.canvas.create_text(x0 + 2, y0, anchor=SW, text=str(random_list[i]))

    def run_algorithm(self):
        print(f"{self.algorithm_value.get()}")

