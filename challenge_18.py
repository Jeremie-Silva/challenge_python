"""Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

https://pythonprinciples.com/challenges/Boolean-and/
"""


def triple_and(param_one, param_two, param_three):
	return all([param_one, param_two, param_three])

	# return param_one and param_two and param_three


triple_and(0,1,0)
