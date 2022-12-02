# https://adventofcode.com/2022/day/2
from enum import IntEnum
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    with open(file_name) as ifile:
        return ifile.readlines()


class Game(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


ENCODING = {
    'A': Game.ROCK,
    'B': Game.PAPER,
    'C': Game.SCISSORS,
    'X': Game.ROCK,
    'Y': Game.PAPER,
    'Z': Game.SCISSORS
}

WINS = {
    Game.ROCK: Game.PAPER,
    Game.PAPER: Game.SCISSORS,
    Game.SCISSORS: Game.ROCK,
}

LOSES = {value: key for key, value in WINS.items()}


def points(player_a: Game, player_b: Game):
    if player_a == player_b:
        return 3 + player_b

    if WINS[player_a] == player_b:
        # B wins
        return player_b + 6

    return player_b


def points2(player_a: Game, result: str):
    if result == 'Y':
        # Tie
        return player_a + 3
    if result == 'Z':
        # Win
        return WINS[player_a] + 6
    return LOSES[player_a]


def part1(file_name: str):
    lines = read_lines_from_file(file_name)
    score = 0
    for line in lines:
        line = line.split()
        player_a, player_b = ENCODING[line[0]], ENCODING[line[1]]
        score += points(player_a, player_b)
    print(score)


def part2(file_name: str):
    lines = read_lines_from_file(file_name)
    score = 0
    for line in lines:
        line = line.split()
        player_a, result = ENCODING[line[0]], line[1]
        score += points2(player_a, result)
    print(score)


if __name__ == '__main__':
    part1('example.txt')
    part1('input.txt')
    print('--------')
    part2('example.txt')
    part2('input.txt')
