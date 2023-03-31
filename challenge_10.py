"""Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]

https://pythonprinciples.com/challenges/Flatten-a-list/
"""

def flatten(complex_list):
	new_list = []
	for element in complex_list:
		for sub_element in element:
			new_list.append(sub_element)
	return new_list

	# return [sub_element for element in complex_list for sub_element in element]


flatten([[1, 2], [3, 4]])