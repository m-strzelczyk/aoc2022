# https://adventofcode.com/2022/day/6
from collections import deque, defaultdict
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


def task(message: str, packet_size: int):
    counter = defaultdict(int)
    buffer = deque(message[:packet_size])
    for letter in buffer:
        counter[letter] += 1
    for i, letter in enumerate(message[packet_size:], packet_size):
        if all(counter[letter] == 1 for letter in buffer):
            print(i)
            return i
        counter[buffer.popleft()] -= 1
        counter[letter] += 1
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
