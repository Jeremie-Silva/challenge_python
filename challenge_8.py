"""Counting syllables
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.

https://pythonprinciples.com/challenges/Counting-syllables/
"""

def count(word_syllables):
	syllables_counter = 1
	for character in word_syllables:
		if character == "-":
			syllables_counter += 1
	return syllables_counter

	# return len([character for character in word_syllables if character == "-"]) +1
	# return len(word_syllables.split("-"))


print(count("ho-tel"))