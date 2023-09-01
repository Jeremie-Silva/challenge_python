"""Challenge 01
Given a dictionary `D`.
Create a list of all the keys without the values.
## Test
Given a dictionary `D` -> {"name": "xathrya", "hp": "100", "mp": "32"}
should produce -> [ "name", "hp", "mp" ]
"""

existent_dict: dict = {"name": "xathrya", "hp": "100", "mp": "32"}


def convert_dict_to_key_list(d: dict):
    return list(d.keys())


print(convert_dict_to_key_list(existent_dict))

# print((lambda x: list(x.keys()))(existent_dict))
