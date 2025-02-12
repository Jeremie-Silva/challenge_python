"""Count the appearance of each letter in a text"""
import string


text: str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

alphabet: dict = {letter: 0 for letter in string.ascii_lowercase}


def count_appearance_of_letters(text: str) -> dict:
    for letter in text.lower():
        if letter in string.ascii_lowercase:
            alphabet[letter] += 1
    return alphabet


if __name__ == "__main__":
    result: dict = count_appearance_of_letters(text=text)
    print(result)
