# https://adventofcode.com/2022/day/1

def main(input_file: str):
    groups = []
    last_group = 0
    with open(input_file) as infile:
        for line in infile.readlines():
            if line.strip() == "":
                groups.append(last_group)
                last_group = 0
            else:
                last_group += int(line)
    groups.append(last_group)
    # Part two can be done more efficiently, by looking just for top 3 groups, instead of fully sorting.
    print(f"Part one answer: {max(groups)}, part two answer: {sum(sorted(groups, reverse=True)[:3])}")


if __name__ == '__main__':
    print("Part one:")
    main('example1.txt')
    main('input1.txt')
