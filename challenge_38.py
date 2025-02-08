"""Search a file in folder continuously refreshed"""
import os
import time


filename_path: str = "./exist.txt"
refresh_timing: int = 5


def is_file_exist(filename_path: str) -> bool:
    return os.path.exists(filename_path)


if __name__ == "__main__":
    while not is_file_exist(filename_path):
        print("Refreshed")
        time.sleep(refresh_timing)
    print("File exists !")
