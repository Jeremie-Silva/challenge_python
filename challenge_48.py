"""Check if a sentence is a pangramme"""
import string


chars: list[str] = list(string.ascii_lowercase)
sentence: str = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"


def is_pangramme(sentence: str) -> bool:
    for letter in list(string.ascii_lowercase):
        if letter not in sentence.lower():
            return False
    return True


if __name__ == "__main__":
    result: bool = is_pangramme(sentence=sentence)
    print(result)
