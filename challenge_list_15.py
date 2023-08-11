"""Challenge 15
Given an integer `N` and `K`. Build list of number starting at 1 and up to
but not including `N`. The list also exclude any number which is multiple of `K`.
    Test
Given an integer `N = 15` and `K = 4`.
The list should be `[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14]`
    Remarks
Generating a list with a criteria.
"""

end: int = 15
exclude: int = 4


def list_builder_with_value_excluded(end: int, exclude: int) -> list[int]:
    return [num for num in range(1, end) if num % exclude != 0]


results = list_builder_with_value_excluded(end, exclude)
print(results)










