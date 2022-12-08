puzzle = open("./input.txt", "r").read()

# part 1

all_lines = puzzle.split("\n")

from collections import Counter

dirs: Counter[str] = Counter()

MAX_SIZE = 100_000

current_dir: list[str] = []  # we will be modifying this a lot
for line in all_lines:
    if line.startswith("$ cd "):
        directory = line.split(" ")[-1]

        if directory == "..":
            current_dir.pop()
            continue

        current_dir.append(directory)
    if line[0].isdigit():
        num = line.split(" ")[0]
        # this is how the linux kernel does it, right?
        for index, this_dir in enumerate(current_dir):
            dirs[str(current_dir[: index + 1])] += int(num)

print(sum(size for size in dirs.values() if size <= MAX_SIZE))

# part 2

ENOUGH = 70_000_000 - 30_000_000
ROOT = dirs["['/']"]  # lmfao this is what I get

print(min(size for size in dirs.values() if ROOT - size <= ENOUGH))
