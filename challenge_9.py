"""Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

https://pythonprinciples.com/challenges/Anagrams/
"""


def is_anagram(string_one, string_two):
	if len(string_one) == len(string_two):
		for letter in string_one:
			try:
				assert string_one.count(letter) == string_two.count(letter)
			except:
				return False
		return True
	return False

	# return sorted(string_one) == sorted(string_two)


is_anagram("typhoon", "opython")