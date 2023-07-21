"""Challenge 00
Given integer `N`.
Generate list of string with length exactly `N`. Each element of string is
lowercase alphabet (a-z).
Save the list as file with each line contain only a string.

    Test
Given `N = 2`, should produce `[ aa, ab, ac, ... , zy, zz ]`

    Remarks
Brute force is an attempt to try all possibilities of states to crack 
verification system. The attack is based on trial and error. The heart of 
this attack is wordlist, a large amount of words that will be verified one by 
one.
Larger wordlist will raise the chance of success but would require longer 
time. Therefore, creating a correct wordlist is essentially useful.
One approach is to create all words from all possible characters on certain 
length. This require large space to store the result.
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = 4
combinations = []


def bruteforce(character_list: list, lenght: int, combinations: list, word=""):
    if len(word) <= lenght:
        for character in character_list:
            bruteforce(character_list, lenght, combinations, word+character)
        if len(word) == lenght:
            combinations.append(word)


bruteforce(alphabet, n, combinations)


print(combinations)
print(len(combinations))
print(len(alphabet)**n)
