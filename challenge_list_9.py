"""Challenge 08
Given `L`, a 2-dimension list (list of list) with various length.
Concatenate all items and make 1-dimension list.
    Testing
Given a list of list of integer -> [ [2, 4, 3], [1, 5, 6], [9], [7, 9] ]
which will produce -> [ 2, 4, 3, 1, 5, 6, 9, 7, 9 ]
    Remarks
Flatten the shallow list. Flattening is creating a new list
by combining (concatenating) all member of list. This is useful if you have
large results from different sources and only interest in the item itself.
Processing 1-dimension list is simpler than 2-dimension list.
"""


l: list = [[2, 4, 3], [1, 5, 6], [9], [[[[[7, 9]]]]]]


def aggregate_lists(global_list: list[int] | list[list]) -> list[int]:
    results = []
    for item in global_list:
        if type(item) == int:
            results.append(item)
        if type(item) == list:
            results += aggregate_lists(item)
    return results


results = aggregate_lists(l)
print(results)
