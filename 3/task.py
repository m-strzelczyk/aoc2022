# https://adventofcode.com/2022/day/3
import string
from typing import List

LETTERS = string.ascii_lowercase + string.ascii_uppercase
LOWERCASE_OFFSET = ord('a') - 1
UPPERCASE_OFFSET = ord('A') - 27


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.read().splitlines(keepends=False)


def task1(file_name: str):
    lines = read_lines_from_file(file_name)
    score = 0
    for line in lines:
        common_letter: str = set(line[:len(line)//2]).intersection(line[len(line)//2:]).pop()
        if common_letter.islower():
            score += ord(common_letter) - LOWERCASE_OFFSET
        else:
            score += ord(common_letter) - UPPERCASE_OFFSET
    print(score)


def task2(file_name: str):
    lines = read_lines_from_file(file_name)
    score = 0
    # Can use batched or grouper from
    # https://docs.python.org/3/library/itertools.html#itertools.islice
    for group in zip(*([iter(lines)]*3)):
        e1, e2, e3 = map(set, group)
        badge = e1.intersection(e2).intersection(e3).pop()
        if badge.islower():
            score += ord(badge) - LOWERCASE_OFFSET
        else:
            score += ord(badge) - UPPERCASE_OFFSET
    print(score)


if __name__ == '__main__':
    task1('example.txt')
    task1('input.txt')
    print('----')
    task2('example.txt')
    task2('input.txt')
