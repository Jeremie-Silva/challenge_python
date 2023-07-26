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


def factors_of_number(N: int) -> list[int]:
    factors_list = []
    for i in range(1, N):
        if N % i == 0:
            factors_list.append(i)
    return factors_list


print(factors_of_number(N))


# TODO: fonction recursive pour chaque nombre, dans une boucle