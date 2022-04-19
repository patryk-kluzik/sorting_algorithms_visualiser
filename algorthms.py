from random import randint
import time


def get_random_list(list_size: int, min_value: int, max_value: int) -> list:
    return [randint(min_value, max_value) for _ in range(list_size)]


def bubble_sort(unsorted_list: list, draw_data, sorting_speed: float):
    """
    Bubble sort algorithm compares the next element and swaps them if the current element is bigger than the next.
    This repeats until the end of the list or if no swaps were done (list is already sorted).
    With each iteration we loop from the start of the list but decrease the range by 1 (the last element is already the
    largest element in the list therefore no swaps need to be done).
    The bubble sort is complete when no more swaps are performed during an iteration.
    :param draw_data: function which draws the data to the screen
    :param sorting_speed: speed at which the program will sleep to show the sorting process
    :param unsorted_list: an unsorted list of integers
    :return: a list which is sorted using bubble sort
    """
    is_sorted = False
    range_length = len(unsorted_list) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(range_length):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i + 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i + 1]
                draw_data(unsorted_list, ["green" if x == i+1 else "red" for x in range(len(unsorted_list))])
                time.sleep(sorting_speed)
                is_sorted = False
        range_length -= 1
    draw_data(unsorted_list, ["green" for _ in range(len(unsorted_list))])
