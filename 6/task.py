# https://adventofcode.com/2022/day/6
from collections import deque, defaultdict
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


class MyCounter:
    OFFSET = ord('a')

    def __init__(self):
        self._memory = [0]*26
        self._uniques = 0

    def add(self, key):
        index = ord(key) - self.OFFSET
        if self._memory[index] == 0:
            self._uniques += 1
        self._memory[index] += 1

    def remove(self, key):
        index = ord(key) - self.OFFSET
        self._memory[index] -= 1
        if self._memory[index] == 0:
            self._uniques -= 1

    def number_of_unique_keys(self) -> int:
        return self._uniques


def task(message: str, packet_size: int):
    counter = MyCounter()
    buffer = deque(message[:packet_size])
    for letter in buffer:
        counter.add(letter)
    for i, letter in enumerate(message[packet_size:], packet_size):
        if counter.number_of_unique_keys() == packet_size:
            print(i)
            return i
        counter.remove(buffer.popleft())
        counter.add(letter)
        buffer.append(letter)
    raise RuntimeError


if __name__ == '__main__':
    task('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
    task('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
    task('nppdvjthqldpwncqszvftbrmjlhg', 4)
    task('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
    task('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)
    task(open('input.txt').read(), 4)
    #....
    task('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
    task('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
    task('nppdvjthqldpwncqszvftbrmjlhg', 14)
    task('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
    task('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)
    task(open('input.txt').read(), 14)
