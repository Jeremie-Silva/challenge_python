"""Challenge 07
Given a list `L`. Shuffle the position of all items.
Shuffling is repositioning each item to random place.
Modification is in-place and no new list created.
    Test
Given a list of integer `L` -> [ 3, 2, 6, 7, 2 ]
One of possible result from shuffling is -> [ 6, 2, 7, 2, 3 ]
"""

from random import shuffle

l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def shuffle_list(integer_list: list[int]) -> None:
    shuffle(integer_list)


print(l)
shuffle_list(l)
print(l)
