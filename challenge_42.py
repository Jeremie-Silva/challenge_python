"""Generate random password"""
import string
from random import randint


lenght: int = 16
chars: list[str] = list(string.ascii_letters + string.digits + string.punctuation)


def generate_random_password(chars: list[str], lenght: int = 16) -> str:
    result: str = ""
    for _ in range(lenght):
        result += chars[randint(0, len(chars) - 1)]
    return result


if __name__ == "__main__":
    result: str = generate_random_password(chars=chars, lenght=lenght)
    print(result)
