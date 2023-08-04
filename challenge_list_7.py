"""Challenge 06
Given a list `L`. Choose item randomly from `L`.
Create two version, where:
- chosen item is kept in `L`.
- chosen item is discard from `L`.
"""

from random import randint

l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def remove_item_randomly(integer_list: list[int]) -> list[int]:
    del integer_list[randint(0, len(integer_list)-1)]
    return integer_list


def select_item_randomly(integer_list: list[int]) -> int:
    return integer_list[randint(0, len(integer_list)-1)]


results = remove_item_randomly(l)
print(results)

random_item = select_item_randomly(l)
print(random_item)







