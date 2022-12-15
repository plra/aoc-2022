def read_input(filename):
    with open(filename) as f:
        return [
            tuple(map(eval, pair_str.split("\n")))
            for pair_str in f.read().split("\n\n")
        ]


def listify(p):
    if type(p) == int:
        p = [p]
    return p


def cmp(p, q):
    if type(p) == type(q) == int:
        return (p > q) - (p < q)
    p, q = listify(p), listify(q)
    for i in range(2 ** 63):
        if len(p) <= i < len(q):
            return -1
        elif len(p) == len(q) <= i:
            return 0
        elif len(q) <= i < len(p):
            return 1
        cmp_i = cmp(p[i], q[i])
        if cmp_i != 0:
            return cmp_i
    return 0


if __name__ == "__main__":
    pairs = read_input("input.txt")
    print(sum(i + 1 for i, (p, q) in enumerate(pairs) if cmp(p, q) == -1))
