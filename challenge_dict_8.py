"""Challenge 07
Given two lists `K` and `V`.
Create a dictionary where the key-value pair is combination of `K` and `V` at same index.
Note: handle the case when the length of two lists are not equal.
    Test
Given two list, `K` and `V` -> K = [ "name", "hp", "mp" ] , V = [ "xathrya", "100", "32" ]
will produce new dictionary -> {"name": "xathrya", "hp": "100", "mp": "32"}
    Remarks
Create dictionary by list of keys and values.
"""

k: list[str] = ["name", "hp", "mp"]
v: list[str] = ["xathrya", "100", "32"]


def generate_dict_with_two_lists(list_1: list[str], list_2: list[str]) -> dict:
    return dict(zip(k, v))


print(generate_dict_with_two_lists(k, v))
