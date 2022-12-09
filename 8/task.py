# https://adventofcode.com/2022/day/8
import operator
from collections import defaultdict
from functools import reduce
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.read().strip().splitlines(keepends=False)


def all_rows_and_columns(max_row, max_col):
    for row in range(max_row):
        yield [(row, i) for i in range(max_col)]
        yield [(row, i) for i in reversed(range(max_col))]
    for col in range(max_col):
        yield [(i, col) for i in range(max_row)]
        yield [(i, col) for i in reversed(range(max_row))]

def all_rows_and_columns_with_direction(max_row, max_col):
    for row in range(max_row):
        yield [(row, i) for i in range(max_col)], (0, -1)
        yield [(row, i) for i in reversed(range(max_col))], (0, 1)
    for col in range(max_col):
        yield [(i, col) for i in range(max_row)], (-1, 0)
        yield [(i, col) for i in reversed(range(max_row))], (1, 0)


def task1(input_file: str):
    lines = read_lines_from_file(input_file)

    trees = defaultdict(lambda: float('-inf'))
    for row, line in enumerate(lines):
        for col, character in enumerate(line.strip()):
            trees[row, col] = int(character)

    visible_trees = set()
    for tree_line in all_rows_and_columns(row+1, col+1):
        height = -1
        for tree_pos in tree_line:
            # print(tree_pos)
            if trees[tree_pos] > height:
                visible_trees.add(tree_pos)
                height = trees[tree_pos]

    print(len(visible_trees))


def task2(input_file: str):
    lines = read_lines_from_file(input_file)

    trees = defaultdict(lambda: None)
    for row, line in enumerate(lines):
        for col, character in enumerate(line.strip()):
            trees[row, col] = int(character)

    tree_visibility_map = defaultdict(lambda: {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0})
    for tree_line, direction in all_rows_and_columns_with_direction(row+1, col+1):
        for trow, tcol in tree_line:
            irow, icol = direction
            if trees[trow + irow, tcol + icol] is None:
                tree_visibility_map[trow, tcol][irow, icol] = 0
                continue
            if trees[trow, tcol] <= trees[trow + irow, tcol + icol]:
                tree_visibility_map[trow, tcol][irow, icol] = 1
            else:
                lrow, lcol = trow + irow, tcol + icol
                while trees[trow, tcol] > trees[lrow, lcol]:
                    tree_visibility_map[trow, tcol][irow, icol] += 1
                    lrow, lcol = lrow + irow, lcol + icol
                    if trees[lrow, lcol] is None:
                        break
                else:
                    tree_visibility_map[trow, tcol][irow, icol] += 1

    maxim = -1
    winner = (0, 0)
    for key, value in tree_visibility_map.items():
        if reduce(operator.mul, value.values()) > maxim:
            winner = key
            maxim = reduce(operator.mul, value.values())
    print(winner, maxim, tree_visibility_map[winner])


if __name__ == '__main__':
    task1('example.txt')
    task1('input.txt')
    task2('example.txt')
    task2('input.txt')
