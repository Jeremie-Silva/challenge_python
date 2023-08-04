"""Challenge 05
Given a list `L`. Create a list `U` where the items is unique (not repeating) values from `L`.
    Test
Given a list `L` -> [ 1, 1, 2, 3, 4, 4, 6, 9 ]
extracting all unique values will produce -> [ 2, 3, 6, 9 ]
"""


l: list[int] = [1, 1, 2, 3, 4, 4, 6, 9]


def keep_only_single_items(integer_list: list[int]) -> list[int]:
    # results = []
    # for item in integer_list:
    #     if item in results:
    #         results.remove(item)
    #     else:
    #         results.append(item)
    # return results
    return [item for item in integer_list if integer_list.count(item) == 1]


results = keep_only_single_items(l)
print(results)









