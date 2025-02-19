"""Recreate join() built-in function"""


values: list[str] = ["Bonjour", "tout", "le", "monde"]
separator: str = ":"


def my_join(*args, separator: str = " ") -> str:
    result: str = ""
    for value in args:
        result += value + separator
    return result[:-1]


if __name__ == "__main__":
    result: str = my_join(*values, separator=separator)
    print(result)
