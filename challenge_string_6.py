"""Challenge 09
Given a string with length `N`.
Generate all possible permutation of the string.
    Test
Given the string of length 3 -> ABC
all possible permutation would be -> ABC, ACB, BAC, BCA, CAB, CBA
    Remarks
Permutation is the arrangement of members or elements of a collection,
in regards to the order of the arrangements. Permutation can be done on
selected objects or subset. However, in most case we are interested
in permutating the whole collection.
Permutation of string is one of operation in classic cipher.
Permutation is also used as operation in block cipher,
such as `Substitution-Permutation Network (SPN)`,
where plaintext is rearranged according a rule (Permutation Box).
"""

word: str = "ABC"
word_list: list = []


def permutated_letters(word: str, word_list: list, begin="") -> list[str]:
    if len(word) == 0:
        word_list.append(begin)
    for count, letter in enumerate(word):
        permutated_letters(word[0:count] + word[count+1:], word_list, begin+letter)
    return word_list


def combination_counter_with_range(lenght: int) -> int:
    count = 1
    for i in range(lenght, 0, -1):
        count *= i
    return count


def combination_counter_with_while(lenght: int) -> int:
    count = 1
    while lenght-1 > 0:
        count *= lenght
        lenght -= 1
    return count


result_list: list[str] = permutated_letters(word, word_list)

print(result_list)
print(len(result_list))
print(combination_counter_with_range(len(word)))
print(combination_counter_with_while(len(word)))
