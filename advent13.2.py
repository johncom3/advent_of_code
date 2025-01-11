import re

with open("/Users/jonathanborer/Desktop/Programmieren WI/advent/advent_data/day13.txt") as fin:
    lines = fin.read().strip().split("\n\n")


def parse(x):
    lines = x.split("\n")
    a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
    b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
    p = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
    return a, b, p


prices = []
bad = 0
for a, b, p in [parse(line) for line in lines]:
    p[0] += 10000000000000
    p[1] += 10000000000000

    # a[0] * i + b[0] * j == p[0]
    # a[1] * i + b[1] * j == p[1]

    def verify(i, j):
        if i < 0 or j < 0:
            return False
        return (a[0] * i + b[0] * j == p[0]) and \
               (a[1] * i + b[1] * j == p[1])

    i = (p[0] * b[1] - b[0] * p[1]) // (b[1] * a[0] - b[0] * a[1])
    j = (p[1] - a[1] * i) // b[1]
    # if i <= 0 or j <= 0:
    #     continue
    # if round(i) != int(i) or round(j) != int(j) or i < 0 or j < 0:
    #     continue

    if verify(i, j):
        prices.append(3*int(i) + int(j))

spent = 0
print(sum(prices))
