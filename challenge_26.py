"""Create a pattern with prints"""


n: int = 8
symbole: str = "*"


def print_pattern(max: int, symbole: str) -> None:
    for index in range(max):
        print(index * symbole)

    for index in range(max, 0, -1):
        print(index * symbole)


if __name__ == "__main__":
    print_pattern(max=n,symbole=symbole)
