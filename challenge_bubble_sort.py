"""Recreate an alternative to sort built-in for ints lists, with manual bubble sort"""

data_to_sort: list[int] = [8, 3, 4, 2, 1]
data_to_sort_2: list[int] = [40, 16, 80, 2, 90]



def buble_sort(data: list[int]) -> list[int]:
    swaped: bool = False
    for i in range(len(data) - 1):
        for index in range(len(data) - i - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                swaped = True
        if not swaped:
            break
    return data



if __name__ == "__main__":
    print(data_to_sort)
    data_sorted: list[int] = buble_sort(data=data_to_sort)
    print(data_sorted)

    print(data_to_sort_2)
    data_sorted_2: list[int] = buble_sort(data=data_to_sort_2)
    print(data_sorted_2)
