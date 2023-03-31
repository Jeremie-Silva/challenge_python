"""Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

https://pythonprinciples.com/challenges/Type-check/
"""

def only_ints(param_one, param_two):
	if type(param_one) == int and type(param_two) == int:
		return True
	return False

	# return type(param_one) == int and type(param_two) == int


only_ints(1,2)
