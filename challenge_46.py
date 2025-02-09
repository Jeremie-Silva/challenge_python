"""Reverse words in sentence"""


sentence: str = "Bonjour tout le monde"


def reverse_words(sentence: str) -> str:
    result: list[str] = []
    for word in sentence.split():
        result.insert(0, word)
    result[0] = result[0].title()
    return " ".join(result)


if __name__ == "__main__":
    result: str = reverse_words(sentence=sentence)
    print(result)
