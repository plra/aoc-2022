from p1 import read_instrs, get_xs

WIDTH = 40


def get_drawing(xs):
    s = ""
    for cycle, x in enumerate(xs):
        if abs(x - (cycle % WIDTH)) <= 1:
            s += "#"
        else:
            s += "."
        if (cycle + 1) % WIDTH == 0:
            s += "\n"
    return s


if __name__ == "__main__":
    instrs = read_instrs("input.txt")
    xs = get_xs(instrs)
    print(get_drawing(xs))
