"""Check if all brackets are closed"""


code: str = "print(any(('py' or 'txt') in ext for ext in ['.py', '.obj', '.json'])"


def is_brackets_are_valids(code: str) -> bool:
    left_brackets: int = code.count("(")
    right_brackets: int = code.count(")")
    return left_brackets == right_brackets


if __name__ == "__main__":
    result: bool = is_brackets_are_valids(code=code)
    print(result)
