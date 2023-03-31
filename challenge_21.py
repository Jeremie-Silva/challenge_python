"""Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.

https://pythonprinciples.com/challenges/Solution-validation/
"""

import re
def validate(code_str):
	if "def" not in code_str:
		return "missing def"
	if ":" not in code_str:
		return "missing :"
	if "(" and ")" not in code_str:
		return "missing paren"
	if re.search(r"\(\)", code_str):
		return "missing param"
	if "    " not in code_str:
		return "missing indent"
	if "validate" not in code_str:
		return "wrong name"
	if "return" not in code_str:
		return "missing return"
	return True


validate("    def validate(param): return")
