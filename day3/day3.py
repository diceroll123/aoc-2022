puzzle = open("./input.txt", "r").read()

# part 1

all_lines = puzzle.split("\n")

import string

all_letters = string.ascii_lowercase + string.ascii_uppercase

priorities: list[int] = []

for line in all_lines:
    half_length = len(line) // 2
    first, second = set(line[half_length:]), set(line[:half_length])
    priorities.append(all_letters.index(list(first.intersection(second))[0]) + 1)

print(sum(priorities))

# part 2

total = 0

chunked = [all_lines[i : i + 3] for i in range(0, len(all_lines), 3)]

for lines in chunked:
    sets: list[set[str]] = []
    for line in lines:
        sets.append(set(line))
    first, second, third = sets
    total += (
        all_letters.index(list(first.intersection(second).intersection(third))[0]) + 1
    )

print(total)
