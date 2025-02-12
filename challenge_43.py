"""Generate random password with verifications"""
import string
from random import randint


lenght: int = randint(4, 25)
chars: list[str] = list(string.ascii_letters + string.digits + string.punctuation)


def generate_random_password(chars: list[str], lenght: int = 16) -> str:
    result: str = ""
    for _ in range(lenght):
        result += chars[randint(0, len(chars) - 1)]
    return result


def password_is_valid(password: str, min_lenght: int, min_numbers: int, min_uppers: int) -> bool:
    if len(password) < min_lenght:
        return False
    lenght_numbers: int = sum([1 for char in password if char in string.digits])
    if lenght_numbers < min_numbers:
        return False
    lenght_uppers: int = sum(1 for char in password if char in string.ascii_lowercase)
    if lenght_uppers < min_uppers:
        return False
    return True


if __name__ == "__main__":
    valid_password: bool = False
    while not valid_password:
        result: str = generate_random_password(chars=chars, lenght=lenght)
        if password_is_valid(password=result, min_lenght=8, min_numbers=2, min_uppers=1):
            valid_password = True
    print(result)
