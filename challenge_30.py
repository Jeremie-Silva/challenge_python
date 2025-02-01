"""Create a function to move up in a folder structure"""


path: str = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"


def move_up_by_loop(path: str, up: int = 1) -> str:
    return ("/").join(path.split("/")[:-up])


def move_up_recursively(path: str, up: int = 1) -> str:
    if up == 0:
        return path
    new_path: str = ("/").join(path.split("/")[:-1])
    return move_up_recursively(path=new_path, up=up-1)


if __name__ == "__main__":
    print(path)
    first_results: str = move_up_by_loop(path=path, up=3)
    print(first_results)
    second_results: str = move_up_recursively(path=path, up=3)
    print(second_results)
