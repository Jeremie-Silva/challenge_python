"""Recreate an alternative to list built-in type"""


class CustomList(list):
    def __init__(self, *args):
        super().__init__(arg.upper() for arg in args if isinstance(arg, str))

    def append(self, value):
        if not isinstance(value, int):
            super().append(value)
        return "Nombres entiers interdits"



if __name__ == "__main__":
    custom_list: CustomList = CustomList("Pierre", 12345, "Marie", "Joseph")
    print(f"{custom_list=}")
    print(custom_list.append(12345))
    print(f"{custom_list=}")
