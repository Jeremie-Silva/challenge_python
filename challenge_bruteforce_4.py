"""Challenge 05
Given a word W and a dictionary of alternative characters L.
Generate list of alternative words.
Each word is produced by substitute one character with its alternative character.

    Test
Given word password and list of substitute character as
{'a': ['a','A','@','4'] } should produce :
password
pAssword
p@ssword
p4ssword

    Remarks
Industry standard enforce password to contain letter (lowercase/uppercase), numbers,
and special characters. User might use seasy to remember password related to company name,
pet name, partner name, etc with slight modification.

Our approach for this is to permutate word.
Permutation is substituting a character with alternative characters.
However, creating permutation will have more costs in storage or time.
"""

permutate_character_dict = {
    "a": ["a", "A", "@", "4"],
    "s": ["s", "S", "$", "5"],
    "o": ["o", "O", "°", "0"]
}
word = "password"
combinations = []


def bruteforce(permutate_character_dict: dict, combinations: list, word: str):
    for count, letter in enumerate(word):
        if permutate_character_dict.get(letter):
            for permutate_letter in permutate_character_dict[letter]:
                new_word = word[:count] + permutate_letter + word[count+1:]
                combinations.append(new_word)


bruteforce(permutate_character_dict, combinations, word)


print(combinations)
print(len(combinations))
