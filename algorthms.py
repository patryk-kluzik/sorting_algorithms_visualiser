from random import randint


def get_random_list(list_size: int, min_value: int, max_value: int) -> list:
    return [randint(min_value, max_value) for _ in range(list_size)]


random_unsorted_list = get_random_list(list_size=10, min_value=0, max_value=100)
print(random_unsorted_list)
