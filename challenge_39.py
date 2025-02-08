"""Count the content of a folder"""
import os


path: str = "."


def count_content(path: str = ".") -> dict:
    return {
        "dirs": len(list(os.walk(path))[0][1]),
        "files": len(list(os.walk(path))[0][2]),
    }


if __name__ == "__main__":
    result: dict = count_content(path=path)
    print(result)
