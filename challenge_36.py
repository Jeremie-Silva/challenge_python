"""Find factorial of a number"""


number: int = 5


def factorial(number: int) -> int:
    result: int = 1
    for num in range(1, number + 1):
        result *= num
    return result


if __name__ == "__main__":
    result: int = factorial(number)
    print(result)
