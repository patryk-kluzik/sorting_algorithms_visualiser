import tkinter.ttk
import threading
from algorthms import *
from tkinter import *


class VisualiserUI:

    def __init__(self):
        self.array = []
        self.algorithm_list = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort"]
        self.font = ("Prompt", 10, "normal")
        self.swaps = 0
        self.comparisons = 0
        self.stop = True

        # ------------ root --------------#
        self.window = Tk()
        self.window.title("Sorting Algorithm Visualiser")
        self.window.config(bg="black")
        self.window.resizable(width=False, height=False)
        self.window.minsize(width=900, height=600)

        # ------------ Frame --------------#
        self.frame = Frame(master=self.window, width=600, height=140, bg="grey")
        self.frame.grid(row=0, column=0)

        self.frame_info = Frame(master=self.window, width=300, height=140, bg="black", highlightthickness=1)
        self.frame_info.grid(row=0, column=1)

        # ------------ Canvas --------------#
        self.canvas = Canvas(master=self.window, width=900, height=460, bg="black", highlightthickness=0)
        self.canvas.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        # ------------ Scale --------------#
        self.list_size_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.list_size_scale.config(resolution=1, from_=2, to=200,
                                    font=self.font, label="Array Size",
                                    length=100)
        self.list_size_scale.grid(row=1, column=0, padx=10, pady=5)

        self.min_value_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.min_value_scale.config(resolution=1, from_=0, to=10,
                                    font=self.font, label="Min Value",
                                    length=100)
        self.min_value_scale.grid(row=1, column=1, padx=10, pady=5)

        self.max_value_scale = Scale(master=self.frame, orient=HORIZONTAL)
        self.max_value_scale.config(resolution=1, from_=10, to=100,
                                    font=self.font, label="Max Value",
                                    length=100)
        self.max_value_scale.grid(row=1, column=2, padx=10, pady=5)

        self.sort_speed_scale = Scale(master=self.frame, orient=HORIZONTAL, length=200)
        self.sort_speed_scale.config(resolution=0.05, from_=0.05, to=2,
                                     font=self.font, label="Select Delay [s]")
        self.sort_speed_scale.grid(row=0, column=2, padx=10, pady=5)

        # ------------ Buttons --------------#
        self.generate_button = Button(master=self.frame, text="Generate Array",
                                      font=self.font, command=self.get_array_values)
        self.generate_button.grid(row=1, column=3, padx=10, pady=5)

        self.run_algorithm_button = Button(master=self.frame, text="Run algorith",
                                           font=self.font, command=lambda: self.start_run_algorithm(None))
        self.run_algorithm_button.grid(row=0, column=3, padx=10, pady=5)

        # ------------ Labels --------------#
        self.algorithm_value = tkinter.StringVar()

        self.algorithm_label = Label(master=self.frame, text="Algorithm: ", bg="gray", fg="black", font=self.font)
        self.algorithm_label.grid(row=0, column=0)

        self.algorithm_menu = tkinter.ttk.Combobox(master=self.frame,
                                                   textvariable=self.algorithm_value,
                                                   font=self.font,
                                                   values=self.algorithm_list)
        self.algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
        self.algorithm_menu.current(0)

        self.algorithm_label_info = Label(master=self.frame_info, text=f"", font=self.font,
                                          bg="black", fg="white", width=30)
        self.algorithm_label_info.grid(row=0, column=0)

        self.swaps_label = Label(master=self.frame_info, text=f"Swaps: \t\t\t{self.swaps}\t", font=self.font,
                                 bg="black", fg="white")
        self.swaps_label.grid(row=1, column=0)

        self.comparisons_label = Label(master=self.frame_info, text=f"Comparisons: \t\t{self.comparisons}\t",
                                       font=self.font
                                       , bg="black", fg="white")
        self.comparisons_label.grid(row=2, column=0, pady=25)

        self.window.mainloop()

    def get_array_values(self):
        if self.stop:
            self.array = get_random_list(list_size=self.list_size_scale.get(),
                                         min_value=self.min_value_scale.get(),
                                         max_value=self.max_value_scale.get())
            self.draw_array(random_list=self.array, color_array=["white" for x in range(self.list_size_scale.get())])
        return self.array

    def draw_info(self, swaps, comparisons):

        self.swaps = swaps
        self.comparisons = comparisons

        self.swaps_label.config(text=f"Swaps: \t\t\t{self.swaps}\t")
        self.comparisons_label.config(text=f"Comparisons: \t\t{self.comparisons}\t")

    def draw_array(self, random_list, color_array):
        self.canvas.delete("all")
        offset = 10
        c_width = 900 - (offset / 2)
        c_height = 460
        spacing = 2
        x_width = c_width / self.list_size_scale.get()

        normalised_data = [i / max(random_list) for i in random_list]

        for i, array_height in enumerate(normalised_data):
            x0 = i * x_width + spacing
            y0 = c_height - array_height * c_height
            x1 = (i + 1) * x_width
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline=color_array[i])

        self.window.update_idletasks()

    def start_run_algorithm(self, event):
        global submit_thread
        submit_thread = threading.Thread(target=self.run_algorithm)
        submit_thread.daemon = True
        submit_thread.start()
        self.window.after(0, self.check_submit_thread)

    def check_submit_thread(self):
        if submit_thread.is_alive():
            self.window.after(0, self.check_submit_thread)

    def check_if_algorithm_stopped(self):
        return self.stop

    def stop_algorithm(self):
        self.run_algorithm_button.config(text="Run Algorithm", command=lambda: self.start_run_algorithm(None))
        self.stop = True

    def run_algorithm(self):
        self.stop = False
        self.run_algorithm_button.config(text="Stop Algorithm", command=self.stop_algorithm)
        current_algorithm = self.algorithm_value.get()
        self.algorithm_label_info.config(text=f"{current_algorithm}")
        self.draw_info(swaps=0, comparisons=0)

        speed = self.sort_speed_scale.get()
        if current_algorithm == "Bubble Sort":
            bubble_sort(unsorted_list=self.array, draw_data=self.draw_array,
                        draw_info=self.draw_info, sorting_speed=speed, stop_alg=self.check_if_algorithm_stopped)
        elif current_algorithm == "Insertion Sort":
            insertion_sort(unsorted_list=self.array, draw_data=self.draw_array,
                           draw_info=self.draw_info, sorting_speed=speed, stop_alg=self.check_if_algorithm_stopped)
        elif current_algorithm == "Selection Sort":
            selection_sort(unsorted_list=self.array, draw_data=self.draw_array,
                           draw_info=self.draw_info, sorting_speed=speed, stop_alg=self.check_if_algorithm_stopped)
        elif current_algorithm == "Merge Sort":
            merge_sort(unsorted_list=self.array, left_index=0, right_index=len(self.array) - 1,
                       draw_data=self.draw_array, draw_info=self.draw_info, sorting_speed=speed,
                       stop_alg=self.check_if_algorithm_stopped)

# TODO: fix issue of app crash on mouse click during draw_array
