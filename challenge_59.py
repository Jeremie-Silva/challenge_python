"""Recreate a french alternative to string built-in type"""


class CustomStr(str):
    def majuscule(self):
        return self.upper()

    def minuscule(self):
        return self.lower()

    def titre(self):
        return self.title()



if __name__ == "__main__":
    custom_str: CustomStr = CustomStr("UdeMy")
    print(f"{custom_str=}")
    print(f"{custom_str.majuscule()=}")
    print(f"{custom_str.minuscule()=}")
    print(f"{custom_str.titre()=}")
