# To have some easy to use functions in all tasks
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()
