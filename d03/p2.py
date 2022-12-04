from p1 import priority

GRP_SIZE = 3

sacks = None
with open("input.txt") as f:
    sacks = [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(
        sum(
            priority(set.intersection(*map(set, group)).pop())
            for group in (
                sacks[i : i + GRP_SIZE] for i in range(0, len(sacks), GRP_SIZE)
            )
        )
    )
