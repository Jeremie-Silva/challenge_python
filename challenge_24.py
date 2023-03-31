"""Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".

https://pythonprinciples.com/challenges/Thousands-separator/
"""


def format_number(number):
	number_list = [digit for digit in str(number)]
	modulo_three = len(number_list) % 3
	result = []
	while number_list:
		if modulo_three != 0:
			result.append(number_list[:modulo_three])
			result.append(",")
			number_list = number_list[modulo_three:]
		modulo_three = 3
	result.pop()
	return ''.join([sub_element for element in result for sub_element in element])

	# return "{:,}".format(number)


format_number(1234567)
format_number(12345678)
format_number(123456789)