"""Find file by exploring folders"""
import os


filename: str = "fichier_test.txt"


def find_file_by_exploring_dirs(filename: str, dir_root: str = ".") -> list[str]:
    result: list[str] = []
    for root, dirs, files in os.walk(dir_root):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


if __name__ == "__main__":
    result: list[str] = find_file_by_exploring_dirs(filename=filename)
    print(result)
