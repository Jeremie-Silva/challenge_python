"""Challenge 02
Given a dictionary `D`.
Create a list of all the values without the keys.
    Test
Given a dictionary `D` -> {"name": "xathrya", "hp": "100", "mp": "32"}
should produce -> [ "xathrya", "100", "32" ]
"""

existent_dict: dict = {"name": "xathrya", "hp": "100", "mp": "32"}


def convert_dict_to_values_list(d: dict) -> list:
    return list(d.values())


print(convert_dict_to_values_list(existent_dict))
