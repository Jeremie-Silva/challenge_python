"""Challenge 02
Given a list of integer. Sum all items in odd index (i.e: 1, 3, 5, ...).
Note: first item is index 0.
    Test
Given list of integer -> [ 3, 0, 4, 9, 7, 9, 7, 2, 9, 4, 1, 4, 2, 5, 5, 7, 4, 0, 6, 9 ]
the sum of odd-index value is: `50`
    Remarks
Fold or accumulate. Get single result (conclusion) by combining multiple objects.
"""


l: list[int] = [3, 0, 4, 9, 7, 9, 7, 2, 9, 4, 1, 4, 2, 5, 5, 7, 4, 0, 6, 10]


def sum_of_odd_index(integer_list: list[int]) -> int:
    return sum([item for index, item in enumerate(integer_list) if index % 2 == 1])


results = sum_of_odd_index(l)
print(results)
