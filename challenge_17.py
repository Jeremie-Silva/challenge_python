"""All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.

https://pythonprinciples.com/challenges/All-equal/
"""


def all_equal(items):
	try:
		for item in items:
			assert items[0] == item
		return True
	except:
		return False

	# return len([item for item in items if item == items[0]]) == len(items)

	# return all(item1 == item2 for item1 in items for item2 in items)


all_equal([1,1,1])