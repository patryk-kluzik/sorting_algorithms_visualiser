from random import choice, randint, randrange


def get_random_list(list_size: int, min_value: int, max_value: int) -> list:
    random_list = []
    for i in range(list_size):
        random_list.append(randint(min_value, max_value))
    return random_list


random_unsorted_list = get_random_list(list_size=10, min_value=0, max_value=100)
print(random_unsorted_list)
