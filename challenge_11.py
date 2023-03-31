"""Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.

https://pythonprinciples.com/challenges/Minmaxing/
"""

def largest_difference(numbers_list):
	return max(numbers_list) - min(numbers_list)


largest_difference([55, 12, -21, 99])