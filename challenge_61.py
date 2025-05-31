"""Recreate an alternative to list built-in type"""


class CustomList(list):
    def __init__(self, *args):
        super().__init__(arg for arg in set(args) if isinstance(arg, str))

    def append(self, value):
        if not isinstance(value, int):
            if value in self:
                return "valeur déjà présente"
            super().append(value)
        return "Nombres entiers interdits"



if __name__ == "__main__":
    custom_list: CustomList = CustomList("Pierre", "Pierre", 12345, "Marie", "Joseph")
    print(f"{custom_list=}")
    print()
    print(custom_list.append(12345))
    print(custom_list.append("Pierre"))
    print()
    print(f"{custom_list=}")
