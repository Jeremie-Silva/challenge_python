"""Recreate an alternative to split built-in function"""


def custom_split_1(text: str, separator: str) -> list[str]:
    result: list[str] = []
    last_index: int = -1
    for index, value in enumerate(list(text)):
        if value == separator:
            result.append(text[last_index + 1 : index])
            last_index = index
    result.append(text[last_index + 1 :])
    return result


def custom_split_2(text: str, separator: str) -> list[str]:
    result: list[str] = []
    current_word: str = ""

    for letter in text:
        if letter != separator:
            current_word += letter
        else:
            result.append(current_word)
            current_word: str = ""
    result.append(current_word)
    return result



if __name__ == "__main__":
    value: str = "bonjour-tout-le-monde"
    result: list[str] = custom_split_2(text=value, separator="-")
    print(result)
