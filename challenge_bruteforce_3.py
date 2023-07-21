"""Challenge 03
Given two integers `S` and `E`.
Generate list of string which length is `S` to `E`. Each element of string is lowercase alphabet (a-z).
Save the list as file with each line contain only a string.

    Test
Given `S = 2` and `E = 3`, should produce:
aa, ab, ac, ..., zy, zz
aaa, aab, aac, ..., zzy, zzz

    Remarks
Some systems dictate that the length of the word is in a fix range, no more or no less.
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
begin = 2
end = 3
combinations = []


def first_character(character_list: list, minimum: int):
    return "".join([character_list[0] for _ in range(minimum-1)])


def bruteforce(character_list: list, combinations: list, lenght: int, begin: int, word=""):
    if len(word) <= lenght:
        for character in character_list:
            bruteforce(character_list, combinations, lenght, begin, word + character)
        if len(word) >= begin:
            combinations.append(word)


def combinations_formatter(combinations: list):
    return sorted(combinations, key=lambda x: (len(x), x))


def highest_power(base: int, power: int, power_minimum):
    return sum([base ** number for number in range(1, power + 1) if power_minimum <= number <= power])


bruteforce(alphabet, combinations, end, begin)
combinations = combinations_formatter(combinations)


print(combinations)
print(len(combinations))
print(highest_power(len(alphabet), end, begin))
