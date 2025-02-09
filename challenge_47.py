"""Check if a sentence is a palindrome"""


sentence: str = "Un roc cornu"


def is_palindrome(sentence: str) -> bool:
    right_way: str = sentence.replace(" ", "").lower()
    reversed_way: str = sentence.replace(" ", "").lower()[::-1]
    return right_way == reversed_way


if __name__ == "__main__":
    result: bool = is_palindrome(sentence=sentence)
    print(result)
