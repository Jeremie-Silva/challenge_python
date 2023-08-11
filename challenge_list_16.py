"""Challenge 16
Given a string of comma-separated integers `L`. Instead of an integer,
some elements might be written as range `a-b` (two numbers separated by dash),
with a <> b.
For each ranges, replace with individual numbers in that range.
    Test
Given list `L` -> L = [1,3,5-9,13]
should produce -> [1,3,5,6,7,8,9,13]
    Remarks
Range expansion.
"""


l: str = "1, 3, 5-9, 13"


def list_builder_from_instructions(l: str) -> list[int]:
    results = []
    for item in l.split(", "):
        if "-" in item:
            [results.append(num) for num in range(int(item[0]), int(item[-1])+1)]
        else:
            results.append(int(item))
    return results


results = list_builder_from_instructions(l)
print(results)
