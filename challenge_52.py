"""Recreate is_digit built-in function"""
import string


value: str = "1854274"


def my_is_digit(value: str) -> bool:
    for char in value:
        if char not in string.digits:
            return False
    return True


if __name__ == "__main__":
    result: bool = my_is_digit(value=value)
    print(result)
