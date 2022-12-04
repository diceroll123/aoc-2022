puzzle = open("./input.txt", "r").read()

# part 1

all_lines = puzzle.split("\n")

fully_contained = 0

for line in all_lines:
    pairs = line.split(",")
    first, second = map(int, pairs[0].split("-"))
    third, fourth = map(int, pairs[1].split("-"))
    first_set = set(range(first, second + 1))
    second_set = set(range(third, fourth + 1))

    if first_set.issubset(second_set) or second_set.issubset(first_set):
        fully_contained += 1

print(fully_contained)

# part 2

overlap_at_all = 0

for line in all_lines:
    pairs = line.split(",")
    first, second = map(int, pairs[0].split("-"))
    third, fourth = map(int, pairs[1].split("-"))
    first_set = set(range(first, second + 1))
    second_set = set(range(third, fourth + 1))

    if first_set & second_set:
        overlap_at_all += 1

print(overlap_at_all)
