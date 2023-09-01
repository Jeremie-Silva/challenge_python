"""Challenge 09
Given a list of dictionary `L`. Remove a common key from each items.
There is no guarantee that the key exists on each item (dictionary).
Note: handle exclusion, where certain key is important and must not be removed.
    Test
Given a list -> [{'id':'1', 'room': '404', 'duration': '4'}, {'id':'2', 'room':'405'}]
Removing key `room` from every list item -> [{'id':'1', 'duration': '4'}, {'id':'2'}]
As seen, `id` is important key in this case to identified each item
"""

l: list = [{'id': '1', 'room': '404', 'duration': '4'}, {'id': '2', 'room': '405'}]
k: str = "room"


def remove_item_if_exist(l: list[dict], k: str) -> list[dict]:
    for item in l:
        if item.get(k):
            del item[k]
    return l


print(remove_item_if_exist(l, k))
