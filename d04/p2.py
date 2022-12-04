import re

# len([a, b] & [c, d])
def overlap(a, b, c, d):
    return b >= c and d >= a


if __name__ == "__main__":
    n = 0
    with open("input.txt") as f:
        for line in f:
            a, b, c, d = map(int, re.split(r"\D+", line.strip()))
            n += overlap(a, b, c, d)
    print(n)
