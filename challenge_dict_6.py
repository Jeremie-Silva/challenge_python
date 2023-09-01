"""Challenge 05
Given a dictionary `D` and a string `K`. Delete key `K` if exist.
    Test
Given a dictionary -> {"key1": 0, "key2": 2, "key3": 5}
deleting `key2` will give result -> {"key1": 0, "key3": 5}
"""

existent_dict: dict = {"key1": 0, "key2": 2, "key3": 5}
word: str = "key2"


def remove_key_if_exist(d: dict, key: str) -> dict:
    if d.get(key):
        del d[key]
    return d


print(remove_key_if_exist(existent_dict, word))
