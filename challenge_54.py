"""Create a folder for each letter"""
import string
import os


letters: list[str] = list(string.ascii_uppercase)
base_name: str = "alphabet"


def create_folders(*folders_name, base_folder: str) -> None:
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)
    os.chdir(base_folder)
    for name in folders_name:
        os.mkdir(name)


if __name__ == "__main__":
    create_folders(*letters, base_folder=base_name)
