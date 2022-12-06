puzzle = open("./input.txt", "r").read()

# part 1

for i in range(len(puzzle)):
    window = puzzle[i : i + 4]
    if len(set(window)) == 4:
        print(i + 4)
        break

# part 2

for i in range(len(puzzle)):
    window = puzzle[i : i + 14]
    if len(set(window)) == 14:
        print(i + 14)
        break
