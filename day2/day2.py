puzzle = open("./input.txt", "r").read()

# part 1

R = 1
P = 2
S = 3
W = 6
L = 0
D = 3

points = 0
points += puzzle.count("A X") * (R + D)
points += puzzle.count("A Y") * (P + W)
points += puzzle.count("A Z") * (S + L)
points += puzzle.count("B X") * (R + L)
points += puzzle.count("B Y") * (P + D)
points += puzzle.count("B Z") * (S + W)
points += puzzle.count("C X") * (R + W)
points += puzzle.count("C Y") * (P + L)
points += puzzle.count("C Z") * (S + D)

print(points)

# part 2

points = 0
points += puzzle.count("A X") * (S + L)
points += puzzle.count("A Y") * (R + D)
points += puzzle.count("A Z") * (P + W)
points += puzzle.count("B X") * (R + L)
points += puzzle.count("B Y") * (P + D)
points += puzzle.count("B Z") * (S + W)
points += puzzle.count("C X") * (P + L)
points += puzzle.count("C Y") * (S + D)
points += puzzle.count("C Z") * (R + W)

print(points)
