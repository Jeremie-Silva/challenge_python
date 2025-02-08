"""Generate random octet"""
from random import randint


lenght: int = 8


def generate_random_binary(lenght: int) -> str:
    result: str = ""
    for num in range(lenght):
        result += str(randint(0, 1))
    return result


if __name__ == '__main__':
    result: str = generate_random_binary(lenght)
    print(result)
