"""Create an alternative to str for re implements method add with space added if concatenate is used"""


class SuperStr(str):  # marche aussi avec -> class str(str):
    def __init__(self, message):
        self.message = message

    def __add__(self, word):
        return SuperStr(f"{self.message} {str(word)}")


if __name__ == "__main__":
    super_str: SuperStr = SuperStr("Bonjour")
    print(super_str + "tout" + "le" + "monde")
