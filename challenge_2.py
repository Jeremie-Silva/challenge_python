"""Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
https://pythonprinciples.com/challenges/Middle-letter/
"""

def mid(word):
	if len(word) % 2 == 1:
		midle_letter = len(word)//2
		return word[midle_letter]
	return ""


mid("abc")
mid("aaaa")

