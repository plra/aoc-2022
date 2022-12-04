import re

# [a, b] contains [c, d]
def contains(a, b, c, d):
    return a <= c and b >= d


if __name__ == "__main__":
    n = 0
    with open("input.txt") as f:
        for line in f:
            a, b, c, d = map(int, re.split(r"\D+", line.strip()))
            n += contains(a, b, c, d) or contains(c, d, a, b)
    print(n)
