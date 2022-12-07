# https://adventofcode.com/2022/day/7

from collections import deque
from typing import List, Optional

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


class Node:
    name: str
    size: int
    total_size: int
    children: dict[str, "Node"]
    parent: Optional["Node"]

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.total_size = size
        self.children = {}

    @property
    def is_dir(self) -> bool:
        return bool(self.children.values())

    def add_child(self, child: "Node"):
        self.children[child.name] = child
        child.parent = self

    def update_size(self) -> int:
        self.total_size = self.size
        for child in self.children.values():
            self.total_size += child.update_size()
        return self.total_size


def parse_input(input_file: str) -> Node:
    lines = read_lines_from_file(input_file)

    root = Node('/', 0)
    cwd = root

    for line in lines:
        match line.split():
            case ('$', 'cd', '/'):
                cwd = root
            case ('$', 'cd', '..'):
                cwd = cwd.parent
            case ('$', 'cd', name):
                cwd = cwd.children[name]
            case ('$', 'ls'):
                pass
            case ('dir', name):
                new_node = Node(name, 0)
                cwd.add_child(new_node)
            case (size, name):
                new_node = Node(name, int(size))
                cwd.add_child(new_node)
            case anything_else:
                raise RuntimeError(f"Unknown line format: {anything_else}")

    root.update_size()
    return root


def task1(input_file: str):
    root = parse_input(input_file)

    def traverser(node: Node) -> int:
        score = 0
        if node.total_size <= 100000 and node.is_dir:
            score += node.total_size
        for child in node.children.values():
            score += traverser(child)
        return score

    print(traverser(root))


def task2(input_file: str):
    root = parse_input(input_file)

    current_size = root.total_size
    need_to_delete = NEEDED_SPACE - (TOTAL_SPACE - current_size)
    # print(f"Total space: {TOTAL_SPACE}, used space: {current_size}, "
    #       f"needed space: {NEEDED_SPACE}, need to free: {need_to_delete}")
    # print(f'Need {need_to_delete} bytes.')

    stack: deque[Node] = deque()
    stack.append(root)

    candidates = []

    while stack:
        cwd = stack.pop()
        if cwd.total_size >= need_to_delete:
            candidates.append(cwd)
        else:
            continue

        for child in cwd.children.values():
            if child.is_dir:
                stack.append(child)

    candidates.sort(key=lambda node: node.total_size)

    print(candidates[0].name, candidates[0].total_size)


if __name__ == '__main__':
    task1('example.txt')
    task1('input.txt')
    print('----------')
    task2('example.txt')
    task2('input.txt')
