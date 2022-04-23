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


def insertion_sort(unsorted_list: list, draw_data, sorting_speed: float):
    """
    Insertion sort loops through the entire array, starting with index 1.
    Compare the element in array at index "i" to previous element, swap them if the previous element is larger and
    decrease "i" by 1. Continue to compare element at "i" with the previous element ( i - 1 ), swap them if previous
    element is larger, do this until reaching the start of the list or if the previous element is no longer larger.
    This continues to happen until we loop through the entire list, at which point all elements will be sorted.

    :param unsorted_list: list of unsorted elements
    :param draw_data: function which will draw the data as its being sorted
    :param sorting_speed: delay between drawing data
    """
    sorting_range = range(1, len(unsorted_list))

    for i in sorting_range:
        draw_data(unsorted_list, ["green" if x == i else "red" for x in range(len(unsorted_list))])
        time.sleep(sorting_speed)
        while unsorted_list[i - 1] > unsorted_list[i] and i > 0:
            unsorted_list[i], unsorted_list[i - 1] = unsorted_list[i - 1], unsorted_list[i]
            i -= 1
            draw_data(unsorted_list, ["green" if x == i else "red" for x in range(len(unsorted_list))])
            time.sleep(sorting_speed)

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
        merge_sort(unsorted_list, left_index, middle_index, draw_data, sorting_speed)
        merge_sort(unsorted_list, middle_index + 1, right_index, draw_data, sorting_speed)
        merge(unsorted_list, left_index, middle_index, right_index, draw_data, sorting_speed)


def merge(unsorted_list: list, left_index, middle_index, right_index, draw_data, sorting_speed: float):
    """
    The entire unsorted list is passed into the function. The array is then drawn using the draw data function.
    We split the array into the l_array and r_array (left array takes the values of the unsorted list between
    left index and middle index  while right array is between middle index and right index).

    Then set the l_array_index to 0 and right_array_index to 0, with the sorted_index equal to left_index parameter -
    this determines where the sorting of the array will be taking place.
    Check if the length of both l_array and r_array and longer than their set arrays (is true as index is set to 0
    and the array is populated, but becomes false once the values is compared as the array index is increased and
    becomes equal or greater than the length of the array - for array of size 1 this is true after one comparison).

    If the element of the l_array is smaller or equal to the element of the r_array at their indices, set the value of
    the unsorted_list at index sorted_index equal to the l_array at l_array_index - e.g. if the l_array is [1] and
    r_array is [7] and sorted_index is 0, then we set the unsorted_list at index 0 to l_array at index 0.
    Therefor the array remains unchanged while l_array_index and sorted_index are increased by 1.

    Otherwise, (if the element of the l_array is greater than r_array) we set the value of the unsorted_list at index
    of sorted_index (0) equal to the r_array at r_array index (0) - e.g. if l_array_is [10] amd r_array is [7] and
    sorted_index is 0, then we set the unsorted_list at index 0 to r_array at index r_array 0.
    Therefor the array now has the copied the [7] into the first position, but the 2nd array is still not swapped.
    The first 2 elements of the unsorted_list go from [10,7] to [7,7].

    After this, the array_index and sorted_index are increased by 1, and these checks are continued until
    the array_index is no longer smaller than the list of that array (e.g. if the l_array and r_array have only 1
    element, the loop only happens once, but is either array has more than 1 element, this can loop several times)

    Then we check if the l_array_index and r_array_index are smaller than the length of these arrays.
    If the previous loop is exited because one of the array is no gone through, then the other array will have its
    array index smaller than it's length, where this loop would then happen. In this loop we check for remaining
    elements of that index and set the value of the elements in the unsorted list to the remaining elements of that
    array, increasing both sorted_index and array_index by 1 until we've gone through them all (and the array_index is
    no longer smaller than its length). This would ensure the values of the elements are swapped and the sublist is
    sorted. (e.g. if the r_array was smaller than the l_array, then l_array_index would be 0, r_array_index would be 1 and
    sorted_index would be 1. Therefor, the l_array_index WOULD be smaller than the l_array length, where we would set
    the element at index sorted_index (1) of the unsorted_list equal to element of l_array at l_array_index (0) -)
    so if l_array was [10] and r_array was [7], then after the unsorted_list copied the element of the r_array into
    index 0, the first to elements go from [10,7] to [7,7]. This check would then set the index 1 of the unsorted_list
    to the first element of the l_array , therefore unsorted_list goes from [7,7] to [7,10] completing the swap.)


    :param unsorted_list: a list of unsorted elements
    :param left_index: the left most index passed
    :param middle_index: the middle index between the 2 indexes
    :param right_index: the right most index passed
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


def get_colour_array(length, left_array, middle_array, right_array) -> list:
    """
    This function provides a list of colours that are used in the draw function to display
    what elements of the list are being compared. This function goes through all the elements
    in the list to provide them with colour values. If the element at the index i between left_array and right_array,
    we will colour it as the sublist. If the element at index i is between left_array and middle_array, we will
    colour is as yellow (showing the l_array sublist), else (if i is not smaller than middle_index) we will colour
    it orange (showing the r_array sublist). The rest of the elements will be coloured red, as they are not part of the
    sublists that are being compared.



    :param length: length of the array
    :param left_array: left index of the sublist
    :param middle_array: middle index between the indices
    :param right_array: right index of the sublist
    :return: list of colours for the sorting animation
    """
    colour_array = []

    for i in range(length):
        print(f"l: {left_array}", f"r: {right_array}", middle_array, f"i: {i}", colour_array)
        if left_array <= i <= right_array:
            if left_array <= i <= middle_array:
                colour_array.append("yellow")
            else:
                colour_array.append("orange")
        else:
            colour_array.append("red")
    return colour_array
