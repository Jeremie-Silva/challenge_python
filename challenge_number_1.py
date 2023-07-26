"""Challenge 00
Given two integers `A` and `B`.
Find the `Greatest Common Divisor` between these two.
    Test
Given two integers `A = 15` and `B = 27`. The `GCD` of both integer is 3.
    Remarks
GCD is one of important concept in Discrete Math, especially some topics on Cryptography.
"""

A: int = 15
B: int = 27


def greatest_common_divisor(A: int, B: int) -> int:
    for i in range(1, A):
        if A % i == 0 and B % i == 0:
            result = i
    return result


print(greatest_common_divisor(A, B))
