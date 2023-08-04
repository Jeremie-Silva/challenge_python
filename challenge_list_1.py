"""Challenge 00
Given a list of integer `L`. Get the largest number from the list.
There is no guarantee that the list is in ordered (sorted) condition.
If the largest number appear multiple time, return them all.
    Test
Given a list of integer `L` -> [ 4, 5, 1, 6, 7, 2, 8, 9, 1, 6, 9 ]
the largest number from the list is `9`, so the result is `[9, 9]`.
    Remarks
Filtering item of the list based on some criteria.
The result might be a single item or sublist. The filtering can be thought as simple iteration and processing of each item in the list.
Filtering is useful to obtain right item for the operation such as selecting correct payload based on target.
"""


l: list[int] = [4, 5, 1, 6, 7, 2, 8, 9, 1, 6, 9]


def highest_number(integer_list: list[int]) -> list[int]:
    reference = 0
    results: list[int] = []
    for item in integer_list:
        if item > reference:
            results.clear()
            results.append(item)
            reference = item
        elif item == reference:
            results.append(item)
        else:
            pass
    return results


results = highest_number(l)
print(results)
