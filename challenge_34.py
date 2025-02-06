"""Find all dividers of a number"""

number: int = 50


def find_dividers(number: int) -> list:
    dividers: list[int] = []
    for num in range(2, number):
        if number % num == 0:
            dividers.append(num)
    return dividers


if __name__ == "__main__":
    dividers: list[int] = find_dividers(number=number)
    print(dividers)
