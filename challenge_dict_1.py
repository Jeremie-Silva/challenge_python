"""Challenge 00
Given a dictionary D, pair of string K and V.
Add value V only if the specified key K is not exists. No value replaced.
    Remarks
Conditional insertion.
"""

existent_dict: dict = {"old_key": "old_value"}


def add_value_if_not_exist(d: dict, key: str, value: str) -> dict:
    d.setdefault(key, value)
    # if d.get(key) == None:
    #     d[key] = value
    return d


add_value_if_not_exist(existent_dict, "old_key", "different_value")
add_value_if_not_exist(existent_dict, "new_key", "new_value")
print(existent_dict)
