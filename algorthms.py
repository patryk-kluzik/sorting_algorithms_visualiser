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
                draw_data(unsorted_list, ["green" if x == i + 1 else "red" for x in range(len(unsorted_list))])
                time.sleep(sorting_speed)
                is_sorted = False
        range_length -= 1
    draw_data(unsorted_list, ["green" for _ in range(len(unsorted_list))])


def merge_sort(unsorted_list: list, left_index, right_index, draw_data, sorting_speed: float):
    """
    This function takes a list and splits it's into smaller sublists by calling itself recursively, which then are
    merged by the merge function. The function finds the middle point to divide the array into two halves.
    Then the function is recursively called for the first half, and again for the second half.
    Finally, we call the merge function to merge the these halves, which sorts the sublist.

    E.G.  For a list that has 8 elements, the left index is 0, middle is 3 and right is 7.

    During the first recursion, the left_index is 0 while the right_index is 3. Here the middle_index is now 1.
    The function calls itself, passing 0 and 1 and left and right indexes, but when the function calls itself again,
    but as the middle index is now 0, the left_index isn't smaller than the right so the loop stops.
    Then the second recursion for where the left is the middle_index + 1 and the right index is itself.
    In this example the left index would be 2 (1+1) and the right would be 3. The function calls itself, but now the
    middle index is (2+3) // 2 which returns 2. The function tried to call itself again, the left is 3 (2+1) and the
    right is still 3, but as left is no longer smaller than the right, this stops the loop.

    This then continues for the 2nd half of the array ( here the left array is middle + 1 and right is itself)
    The left index here is then 4 and right is 7, with 5 being the middle array. This then repeats similarly to above,
    until the list cannot be split anymore and the left_array is not longer smaller than the right_array



    :param unsorted_list: a list of unsorted elements
    :param left_index: the left most index (0)
    :param right_index: the right most index (length of the array - 1)
    :param draw_data: function which draws data in the UI class
    :param sorting_speed: float that determines the delay of the sorting speed
    """
    if left_index < right_index:
        middle_index = (left_index + right_index) // 2
        print(left_index, middle_index, right_index)
        merge_sort(unsorted_list, left_index, middle_index, draw_data, sorting_speed)
        merge_sort(unsorted_list, middle_index + 1, right_index, draw_data, sorting_speed)
        merge(unsorted_list, left_index, middle_index, right_index, draw_data, sorting_speed)


def merge(unsorted_list: list, left_index, middle_index, right_index, draw_data, sorting_speed: float):
    """


    :param unsorted_list: a list of unsorted elements
    :param left_index: the left most index (0)
    :param middle_index: the middle index of the array
    :param right_index: the right most index (length of the array - 1)
    :param draw_data: function which draws data in the UI class
    :param sorting_speed: float that determines the delay of the sorting speed
    :return:
    """
    draw_data(unsorted_list, get_colour_array(len(unsorted_list), left_index, middle_index, right_index))
    time.sleep(sorting_speed)

    l_array = unsorted_list[left_index:middle_index + 1]
    r_array = unsorted_list[middle_index + 1:right_index + 1]

    l_array_index = 0
    r_array_index = 0
    sorted_index = left_index

    while l_array_index < len(l_array) and r_array_index < len(r_array):

        if l_array[l_array_index] <= r_array[r_array_index]:
            unsorted_list[sorted_index] = l_array[l_array_index]
            l_array_index += 1
        else:
            unsorted_list[sorted_index] = r_array[r_array_index]
            r_array_index += 1

        sorted_index += 1

    while l_array_index < len(l_array):
        unsorted_list[sorted_index] = l_array[l_array_index]
        l_array_index += 1
        sorted_index += 1

    while r_array_index < len(r_array):
        unsorted_list[sorted_index] = r_array[r_array_index]
        r_array_index += 1
        sorted_index += 1

    draw_data(unsorted_list,
              ["green" if left_index <= x <= right_index else "red" for x in range(len(unsorted_list))])


def get_colour_array(length, left_array, middle_array, right_array):
    colour_array = []

    for i in range(length):
        if left_array <= i <= right_array:
            if left_array <= i <= middle_array:
                colour_array.append("yellow")
            else:
                colour_array.append("orange")
        else:
            colour_array.append("red")
    return colour_array
