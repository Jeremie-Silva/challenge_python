"""Convert sentence to CamelCase format"""


sentence: str = "Phrase en camel case"


def camel_case_converter_for_loop(sentence: str) -> str:
    result: str = ""
    for word in sentence.split():
        result += word.title()
    return result


def camel_case_converter(sentence: str) -> str:
    return sentence.title().replace(" ", "")


if __name__ == "__main__":
    result: str = camel_case_converter(sentence=sentence)
    print(result)
