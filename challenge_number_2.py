"""Challenge 01
Given an integer `N`. List all of its factors.
    Test
Given an integer `N = 120`, which value can be written as `2^3 x 3 x 5` (^ means power).
Then the factors are `2, 3, 5`.
    Remarks
Some number can be decomposed as product (multiplication) of prime numbers.
This process is also known as factorization. Factorization is important process
in Discrete Math especially some topics on Cryptography.
"""

N: int = 120
expected_result = "2^3 x 3 x 5"


def recursive_divider_decomposer(N: int, divider_dict: dict = {}) -> dict:
    for divider in range(2, N+1):
        if N % divider == 0:
            try:
                divider_dict[divider] += 1
            except KeyError:
                divider_dict[divider] = 1
            recursive_divider_decomposer(int(N/divider), divider_dict)
            break
    return divider_dict


def formatting_dividers(divider_dict: dict) -> str:
    result = ""
    for divider, iterations in divider_dict.items():
        result += f"{divider}^{iterations} x "
    return result[:-3]


def check_dividers_result(divider_dict: dict) -> int:
    result = 1
    for divider, iterations in divider_dict.items():
        result *= (divider ** iterations)
    return result


divider_dict: dict = recursive_divider_decomposer(N)

print(divider_dict)
print(formatting_dividers(divider_dict))
print(check_dividers_result(divider_dict))
