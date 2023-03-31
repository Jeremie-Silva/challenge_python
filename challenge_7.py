"""Challenge
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)

https://pythonprinciples.com/challenges/Adding-and-removing-dots/
"""

def add_dots(word):
	new_word = []
	for letter in word:
		new_word.append(letter)
		new_word.append(".")
	new_word.pop()
	return ''.join(new_word)

	# return ".".join(word)

def remove_dots(word):
	new_word = []
	for letter in word:
		if letter != ".":
			new_word.append(letter)
	return ''.join(new_word)

	# return word.replace(".","")



add_dots("test")
remove_dots("t.e.s.t")

assert remove_dots(add_dots("rgrdgdrjkbdrkvgjbrdk")) == "rgrdgdrjkbdrkvgjbrdk"