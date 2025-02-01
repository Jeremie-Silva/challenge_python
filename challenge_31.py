"""Create a function to convert relative path to absolute"""


path: str = "/Users/Thibh/Desktop/Dossier_01/../Tutoriel/Udemy"


def convert_relative_path_to_absolute(path: str) -> str:
    new_path: str = ""
    levels: list[str] = path.split("/")
    for index, level in enumerate(levels):
        if index < len(levels) - 1:
            if levels[index + 1] == ".." or level == "..":
                continue
        new_path += level + "/"
    return new_path[:-1]


if __name__ == "__main__":
    print(path)
    results: str = convert_relative_path_to_absolute(path)
    print(results)
