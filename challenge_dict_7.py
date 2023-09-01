"""Challenge 06
Given a dictionary `D` and value `V`. Delete every key which have value `V`.
Note: as alternative, create new dictionary which had eliminated the keys.
    Test
Given a dictionary -> {"key1":0, "key2":2, "key3":5, "key4":5}
Removing all keys which have value 5 will give result -> {"key1":0, "key2":2}
    Remarks
Filtering by value.
"""

existent_dict: dict = {"key1": 0, "key2": 2, "key3": 5, "key4": 5}
word: str = "5"


def remove_key_if_value_exist(d: dict, value: str) -> dict:
    return {k: v for k, v in d.items() if str(v) != value}


print(remove_key_if_value_exist(existent_dict, word))
