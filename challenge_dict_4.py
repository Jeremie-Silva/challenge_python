"""Challenge 03
Given a number `N`.
Generate a dictionary where the key is a number from `1` to `N` and the value will be square of the key.
    Test
given `N = 5`, the following dictionary will be produced.
{ 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }
    Remarks
Dictionary comprehension to generate dictionary with criteria.
"""

max: int = 5


def generate_dict_with_squares(max: int, min: int = 1) -> dict:
    return {i: i * i for i in range(1, max + 1)}


print(generate_dict_with_squares(max=max))
