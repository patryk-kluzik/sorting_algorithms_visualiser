import tkinter.ttk
from algorthms import *
from tkinter import *


class VisualiserUI:

    def __init__(self):
        self.array = []
        self.algorithm_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort"]

        # ------------ root --------------#
        self.window = Tk()
        self.window.title("Sorting Algorithm Visualiser")
        self.window.config(bg="black")
        self.window.resizable(width=False, height=False)
        self.window.maxsize(width=900, height=600)

        # ------------ Frame --------------#
        self.frame = Frame(master=self.window, width=900, height=200, bg="grey")
        self.frame.grid(row=0, column=0, padx=5, pady=5, )

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
        self.sort_speed_scale.config(resolution=0.05, from_=0.05, to=1, label="Select Speed [s]")
        self.sort_speed_scale.grid(row=0, column=2, padx=20, pady=5)

        # ------------ Buttons --------------#
        self.generate_button = Button(master=self.frame, text="Generate Array", command=self.get_array_values)
        self.generate_button.grid(row=1, column=3)

        self.run_algorithm_button = Button(master=self.frame, text="Run algorith", command=self.run_algorithm)
        self.run_algorithm_button.grid(row=0, column=3)

        # ------------ Labels --------------#
        self.algorithm_value = tkinter.StringVar()

        self.algorithm_label = Label(master=self.frame, text="Algorithm: ", bg="gray")
        self.algorithm_label.grid(row=0, column=0, padx=5, pady=5)

        self.algorithm_menu = tkinter.ttk.Combobox(master=self.frame,
                                                   textvariable=self.algorithm_value,
                                                   values=self.algorithm_list)
        self.algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
        self.algorithm_menu.current(0)

        self.window.mainloop()

    def get_array_values(self):
        self.array = get_random_list(list_size=self.list_size_scale.get(),
                                     min_value=self.min_value_scale.get(),
                                     max_value=self.max_value_scale.get())
        self.draw_array(random_list=self.array, color_array=["red" for x in range(self.list_size_scale.get())])
        return self.array

    def draw_array(self, random_list, color_array):
        self.canvas.delete("all")
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
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0 + 2, y0, anchor=SW, text=str(random_list[i]))

        self.window.update_idletasks()

    def run_algorithm(self):
        algorithm = self.algorithm_value.get()
        speed = self.sort_speed_scale.get()
        if algorithm == "Bubble Sort":
            bubble_sort(unsorted_list=self.array, draw_data=self.draw_array, sorting_speed=speed)
        elif algorithm == "Merge Sort":
            merge_sort(unsorted_list=self.array, left_index=0, right_index=len(self.array)-1, draw_data=self.draw_array, sorting_speed=speed)
        elif algorithm == "Insertion Sort":
            insertion_sort(unsorted_list=self.array, draw_data=self.draw_array, sorting_speed=speed)
        elif algorithm == "Selection Sort":
            selection_sort(unsorted_list=self.array, draw_data=self.draw_array, sorting_speed=speed)
