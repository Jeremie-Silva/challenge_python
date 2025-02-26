"""Find a word in file or subfolder by exploring"""
import os


word: str = "python"
path: str = "/Users/silvajeremie/Desktop/challenge_python"
folder_to_ignore: list[str] = [".", "venv", ".idea", ".git"]


def find_word_by_exploring_dirs(word: str, path: str = ".", folder_to_ignore: list[str] = ["."]) -> list[tuple]:
    results: list[tuple] = []

    for root, dirs, files in os.walk(path):

        path_components: list[str] = os.path.normpath(root).split(os.sep)
        if any(component in folder_to_ignore for component in path_components):
            continue

        for file in files:
            with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                for index, line in enumerate(f):
                    if word in line:
                        results.append((os.path.join(root, file), f"line n°{index + 1}"))

    return results


if __name__ == "__main__":
    results: list[tuple] = find_word_by_exploring_dirs(word=word, path=path, folder_to_ignore=folder_to_ignore)
    for result in results:
        print(result)
