"""Challenge 10
Given a string `S`. Create list of integer. Each element is ASCII representation of `S`.
    Test
Given a string `S` -> "MII"
representing the string as list of character would give -> [ 'M', 'I', 'I' ]
converting each element to integer will produce -> [ 77, 73, 73 ]
"""


word: str = "MII"


def converter_string_to_ascii_code(word: str) -> list[int]:
    return [ord(letter) for letter in word]


result = converter_string_to_ascii_code(word)
print(result)
