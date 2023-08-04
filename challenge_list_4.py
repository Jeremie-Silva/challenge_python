"""Challenge 03
Given a list of string with various length.
Sort (ascending) the list based on their length.
    Test
Given list of string -> [MII-CyberSec, Xathrya, Reversing.ID]
sorting by the length will give result -> [Xathrya, MII-CyberSec, Reversing.ID]
    Remarks
Sort the list based on criteria.
"""


l: list[str] = ["MII-CyberSec", "Xathrya", "Reversing.ID"]


def sorting_by_lenght(string_list: list[str]) -> list[str]:
    return sorted(string_list, key=lambda x: (len(x), x))


results = sorting_by_lenght(l)
print(results)
