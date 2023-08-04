"""Challenge 04
Given a list `L`. Remove the duplicate items on `L`.
    Test
Given a list `L` -> [ 1, 1, 2, 3, 4, 4, 6, 9 ]
removing duplicate items, we produce -> [ 1, 2, 3, 4, 6, 9 ]
"""


l: list[int] = [1, 1, 2, 3, 4, 4, 6, 9]


def remove_duplicate_items(integer_list: list[int]) -> list[int]:
    results = []
    for item in integer_list:
        if item not in results:
            results.append(item)
    return results
    # return list(dict.fromkeys(integer_list))


results = remove_duplicate_items(l)
print(results)






