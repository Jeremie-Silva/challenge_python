"""Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
https://pythonprinciples.com/challenges/Capital-indexes/
"""

def capital_indexes(word):
	list_upper = []
	for index, letter in enumerate(word):
		if letter.isupper():
			list_upper.append(index)
	return list_upper

	# return [index for index, letter in enumerate(word) if letter.isupper()]


capital_indexes('word')