"""Challenge 01
Given a list of integer `L`. Multiplies all items with 3.
    Test
Given a list of integer `L` -> [ 1, 6, 7, 2, 8 ]
the result is -> [ 3, 18, 21, 6, 24 ]
    Remarks
Map or transform. Processing every items on collection in uniform.
Giving same treatment on all elements.
It is also possible to process in concurrent (parallel execution).
Map is useful for applying some action on multiple objects,
such as sending command to connected agents/implants simultaneously.
"""

l: list[int] = [1, 6, 7, 2, 8]


def multiply_each_member(integer_list: list[int], factor: int = 1):
    return [item * factor for item in integer_list]


results = multiply_each_member(l, 3)
print(results)
