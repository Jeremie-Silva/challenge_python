"""Challenge 11
Given two lists `L` & `M`.
Find the common items from two lists.
## Test
Given two list, `L`= [ 1, 2, 3, 4, 5, 6, 7 ] and `M` = [ 2, 6, 10, 12 ]
will produce new list -> [ 2, 6 ]
    Remarks
Finding intersected items.
"""


first_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
second_list: list[int] = [2, 6, 10, 12]


def find_shared_values(a: list[int], b: list[int]) -> list[int]:
    # result_one = [value for value in a if value in b]
    # result_two = [value for value in b if value in a]
    # return list(dict.fromkeys(result_one + result_two))
    return [value for value in a if value in b]


results = find_shared_values(first_list, second_list)
print(results)
