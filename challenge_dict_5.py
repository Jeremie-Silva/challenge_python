"""Challenge 04
Given a string `S`.
Create a dictionary where the key is a character and
the value is the number of its appearance in the string.
Only existing character appear in the dictionary.
    Test
Given a string
"MII Cybersec" will give result -> {
    'M': 1,
    'I': 2,
    ' ': 1,
    'C': 1,
    'y': 1,
    'b': 1,
    'e': 2,
    'r': 1,
    's': 1,
    'c': 1
}
    Remarks
Frequency counting with dictionary.
"""

word: str = "MII Cybersec"


def generate_characters_dict(word: str) -> dict:
    return {letter: word.count(letter) for letter in word}
    # result = {}
    # for letter in word:
    #     if result.get(letter):
    #         result[letter] += 1
    #     else:
    #         result[letter] = 1
    # return result


print(generate_characters_dict(word))
