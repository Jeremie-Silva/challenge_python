"""Add a thousand separator"""


number: int = 52039480394023
separator: str = "."


def insert_separator_slice_method(number: int, separator: str = ",") -> str:
    result: str = ""
    for index, num in enumerate(str(number)[len(str(number))::-1]):
        if index % 3 == 0 and index != 0:
            result += separator
        result += num
    return result[len(str(result))::-1]


def insert_separator_reversed_method(number: int, separator: str = ",") -> str:
    result: str = ""
    for index, num in enumerate(reversed(str(number))):
        if index % 3 == 0 and index != 0:
            result += separator
        result += num
    return result[len(str(result))::-1]


if __name__ == "__main__":
    first_result: str = insert_separator_slice_method(number=number,separator=separator)
    print(first_result)
    second_result: str = insert_separator_reversed_method(number=number,separator=separator)
    print(second_result)
