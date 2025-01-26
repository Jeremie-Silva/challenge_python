"""Calculate the sum of all numbers between 2 limits"""


def calculate_sum_between_limits_with_for_loop(first: int, second: int) -> int:
    result: int = 0
    for i in range(min(first, second), max(first, second) + 1):
        result += i
    return result


def calculate_sum_between_limits_with_sum(first: int, second: int) -> int:
    return sum(range(min(first, second), max(first, second) + 1))



if __name__ == "__main__":
    first_result: int = calculate_sum_between_limits_with_for_loop(first=2, second=6)
    print(first_result)
    second_result: int = calculate_sum_between_limits_with_for_loop(first=6, second=2)
    print(second_result)
    third_result: int = calculate_sum_between_limits_with_sum(first=2, second=6)
    print(first_result)
    fourth_result: int = calculate_sum_between_limits_with_sum(first=6, second=2)
    print(second_result)
