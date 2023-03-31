"""Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.

https://pythonprinciples.com/challenges/Consecutive-zeros/
"""
# import re

def consecutive_zeros(binary_string):
	global_count = 0
	current_count = 0
	for number in binary_string:
		if int(number) == 0:
			current_count += 1
		else:
			current_count = 0
		if current_count > global_count:
			global_count = current_count
	return global_count

	# import re
	# return len(max(re.findall("0+", binary_string), key=len))

	# return max([len(s) for s in binary_string.split("1")])


consecutive_zeros("100000011100011000")