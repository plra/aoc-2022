def priority(item: str):
    if item.islower():
        return ord(item) - ord("a") + 1
    elif item.isupper():
        return ord(item) - ord("A") + 27


sack_pairs = None
with open("input.txt") as f:
    sack_pairs = [line.strip() for line in f.readlines()]

if __name__ == "__main__":
    print(
        sum(
            priority((set(sack_1) & set(sack_2)).pop())
            for sack_1, sack_2 in (
                (sack_pair[: len(sack_pair) // 2], sack_pair[len(sack_pair) // 2 :])
                for sack_pair in sack_pairs
            )
        )
    )
