# https://adventofcode.com/2022/day/4
import re
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


def task1(input_file: str):
    lines = read_lines_from_file(input_file)
    line_re = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    score = 0
    for line in lines:
        start_a, end_a, start_b, end_b = map(int, line_re.match(line).groups())
        if (start_a <= start_b <= end_b <= end_a) or (start_b <= start_a <= end_a <= end_b):
            score += 1

    print(score)


def task2(input_file: str):
    lines = read_lines_from_file(input_file)
    line_re = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    score = 0
    for line in lines:
        start_a, end_a, start_b, end_b = map(int, line_re.match(line).groups())
        if end_a < start_b or end_b < start_a:
            continue
        score += 1
    print(score)


if __name__ == '__main__':
    task1('example.txt')
    task1('input.txt')
    task2('example.txt')
    task2('input.txt')
