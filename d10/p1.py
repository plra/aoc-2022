def read_instrs(filename):
    with open(filename) as f:
        return [
            (line[:4], int(line[5:]) if line.startswith("addx") else None) for line in f
        ]


# Values of x _during_ cycle i (zero-indexed)
def get_xs(instrs):
    x = 1
    states = []
    for cmd, v in instrs:
        if cmd == "noop":
            states.append(x)
        elif cmd == "addx":
            states.append(x)
            states.append(x)
            x += v
    return states


if __name__ == "__main__":
    instrs = read_instrs("input.txt")
    xs = get_xs(instrs)
    print(sum((i + 1) * xs[i] for i in range(19, len(xs), 40)))
