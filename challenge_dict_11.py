"""Challenge 10
Given two lists `N` and `C`.
Create a new list of dictionaries. The dictionary has two entries, `name` and `code`.
The `name` is assigned by element of `N` and `code` is assigned by element of `C`.
Note: `N` and `C` is guaranteed to be equal length.
    Test
Given two list, `N` and `C` -> N = [ "black", "red", "maroon", "yellow" ]
C = [ "#000000", "#FF0000", "#800000", "#FFFF00" ]
will produce new list
[ {'name': 'Black', 'code': '#000000'},
  {'name': 'Red', 'code': '#FF0000'},
  {'name': 'Maroon', 'code': '#800000'},
  {'name': 'Yellow', 'code': '#FFFF00'} ]
    Remarks
Create a new type of collection by list existing of data.
"""

names: list = ["black", "red", "maroon", "yellow"]
codes: list = ["#000000", "#FF0000", "#800000", "#FFFF00"]


def generate_dict_with_code_and_name(l1: list, l2: list) -> list[dict]:
    return [{"name": i1, "code": i2} for i1, i2 in zip(l1, l2)]


print(generate_dict_with_code_and_name(names, codes))
