""" Challenge 01
Given integer `N`.
Generate list of string which length is `1` to `N`. Each element of string is 
lowercase alphabet (a-z).
Save the list as file with each line contain only a string.

    Test
Given `N = 3`, should produce:
a, b, c, ..., z,
aa, ab, ac, ..., zy, zz
aaa, aab, aac, ..., zzy, zzz

    Remarks
When the length is unknown, then one should generate all words in various 
length.
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = 4
combinations = []


def bruteforce(character_list: list, combinations: list, lenght: int, word=""):
    if len(word) <= lenght:
        for character in character_list:
            bruteforce(character_list, combinations, lenght, word + character)
        combinations.append(word)


def combinations_formatter(combinations: list) -> list:
    combinations.remove("")
    return sorted(combinations, key=lambda x: (len(x), x))


def highest_power(base: int, power: int) -> int:
    return sum(base ** i for i in range(1, power + 1))


bruteforce(alphabet, combinations, n)
combinations = combinations_formatter(combinations)


print(combinations)
print(len(combinations))
print(highest_power(len(alphabet), n))
