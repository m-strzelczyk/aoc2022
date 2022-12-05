# https://adventofcode.com/2022/day/5
import re
from collections import deque
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


def build_stacks(stack_lines: List[str]) -> List[deque]:
    number_of_stacks = stack_lines[-1].count(']')
    stacks = [deque() for _ in range(number_of_stacks)]

    for line in stack_lines:
        for i in range(number_of_stacks):
            try:
                if line[i*4+1] == ' ':
                    continue
                stacks[i].append(line[i*4+1])
            except IndexError:
                # My editor automatically removes spaces from ends of lines
                # in the input from the website, there are spaces
                continue

    return stacks


def task(input_file: str, part_2: bool):
    lines = read_lines_from_file(input_file)

    stack_number_line = None
    stacks_lines, instructions = [], []

    for i, line in enumerate(lines):
        if line[1] == '1':
            stack_number_line = i
            break

    stacks_lines = lines[:stack_number_line]
    instructions = lines[stack_number_line+2:]

    stacks = build_stacks(stacks_lines)

    instr_re = re.compile(r"move (\d+) from (\d+) to (\d+)")

    elems = deque()
    for instruction in instructions:
        icount, ifrom, ito = map(int, instr_re.match(instruction).groups())
        if part_2:
            for _ in range(icount):
                elems.append(stacks[ifrom-1].popleft())
            for _ in range(icount):
                stacks[ito-1].appendleft(elems.pop())
        else:
            for _ in range(icount):
                elem = stacks[ifrom-1].popleft()
                stacks[ito-1].appendleft(elem)

    for stack in stacks:
        print(stack[0], end='')
    print()


if __name__ == '__main__':
    task('example.txt', False)
    task('input.txt', False)
    task('example.txt', True)
    task('input.txt', True)
