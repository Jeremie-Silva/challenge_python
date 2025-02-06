"""Find all dividers of a number if not multiple of another number"""

numbers: list[int] = range(1, 1000)
filter_multiple: int = 7


def find_dividers_filter_multiple(numbers: list[int], multiple_of: int, not_multiple_of: int) -> list:
    dividers: list[int] = []
    for num in numbers:
        if num % multiple_of == 0 and num % not_multiple_of != 0:
            dividers.append(num)
    return dividers


if __name__ == "__main__":
    dividers: list[int] = find_dividers_filter_multiple(numbers=numbers, multiple_of=7, not_multiple_of=3)
    print(dividers)