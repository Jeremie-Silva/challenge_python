"""Count occurrences of a word in text"""


text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore " \
                     "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
                     "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
                     "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " \
                     "mollit anim id est laborum."
target: str = "elit"


def count_occurrences(target: str, text: str) -> int:
    result: int = 0
    for word in text.replace(",", "").split():
        if word == target:
            result += 1
    return result


if __name__ == "__main__":
    result: int = count_occurrences(target=target, text=text)
    print(result)
