puzzle = open("./input.txt", "r").read()

# part 1

import re


def make_crates():
    # i'm hardcoding the starting crates, parsing this sucks
    # for part 1 this was not a method, it was crates=[...]
    # added it because copying lists also sucks
    return [
        ["Z", "T", "F", "R", "W", "J", "G"],
        ["G", "W", "M"],
        ["J", "N", "H", "G"],
        ["J", "R", "C", "N", "W"],
        ["W", "F", "S", "B", "G", "Q", "V", "M"],
        ["S", "R", "T", "D", "V", "W", "C"],
        ["H", "B", "N", "C", "D", "Z", "G", "V"],
        ["S", "J", "N", "M", "G", "C"],
        ["G", "P", "N", "W", "C", "J", "D", "L"],
    ]


crates = make_crates()

moves = puzzle.split("\n\n")[1].split("\n")

for move in moves:
    amount, move_from, move_to = map(int, re.findall(r"\d+", move))
    for _ in range(amount):
        crates[move_to - 1].append(crates[move_from - 1].pop())

print("".join([c[-1] for c in crates]))

# part 2

crates2 = make_crates()

for move in moves:
    amount, move_from, move_to = map(int, re.findall(r"\d+", move))
    crate_stack = crates2[move_from - 1][-amount:]
    del crates2[move_from - 1][-amount:]
    crates2[move_to - 1].extend(crate_stack)

print("".join([c[-1] for c in crates2]))
