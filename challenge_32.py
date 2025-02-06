"""Create a function to write in a file"""


path: str = "fichier_test.txt"
content: str = "challenge_32"


def write_in_file(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    write_in_file(path=path, content=content)
