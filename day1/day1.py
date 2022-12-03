puzzle = open("./input.txt", "r").read()

# part 1
elves = puzzle.split("\n\n")

sums = [sum(map(int, elf.split("\n"))) for elf in elves]

sums.sort()

print(sums[-1])

# part 2

print(sum(sums[-3:]))
