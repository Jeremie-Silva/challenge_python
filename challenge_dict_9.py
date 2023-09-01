"""Challenge 08
Given a list of dictionary `L` and key `K`. Sort the list by the value of key `K`.
    Test
Given a list -> [{'key': 1}, {'key': 10}, {'key': 5}]
using `key` as pivot, the list would be sorted as -> [{'key': 1}, {'key': 5}, {'key': 10}]
    Remarks
Sort list of dictionary. Dictionary can be a representation of JSON.
"""

l: list = [{'key': 1}, {'key': 10}, {'key': 5}]
k: str = "key"


def sort_list(l: list[dict], k: str) -> list[dict]:
    return sorted(l, key=lambda x: x.get("key"))


print(sort_list(l, k))
