"""Create a function to read in a file"""


path: str = "fichier_test.txt"
content: str = "False"


def write_in_file(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)


def read_in_file(path: str) -> list:
    with open(path, "r") as file:
        content: list = file.read()
    return content


if __name__ == "__main__":
    write_in_file(path=path, content=content)
    content: list = read_in_file(path=path)
    print(content)
