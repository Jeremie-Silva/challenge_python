"""Challenge 09
Given two integers `S` and `E`, with `S` less than `E`.
Create a list of unique (non-repeating) integers with value from `S` to `E`.
The position of the value is random.
    Test
Given integer `S = 3`, `E = 10`. One of possible result will be -> [ 3, 8, 7, 4, 10, 9, 6, 5 ]
From `S = 3` to `E = 10`, there are 8 integers.
"""

from random import shuffle


min: int = 3
max: int = 10


def generate_shuffled_list(min: int, max: int) -> list[int]:
    results = [item for item in range(min, max + 1)]
    shuffle(results)
    return results


results = generate_shuffled_list(min, max)
print(results)
