SOURCE = (500, 0)


def linspace(a, b):
    if a > b:
        a, b = b, a
    return range(a, b + 1)


def read_grid(filename):
    grid = {SOURCE: "+"}
    with open(filename) as f:
        for path in f:
            knots = [tuple(map(int, s.split(","))) for s in path.strip().split(" -> ")]
            for i in range(1, len(knots)):
                x_i, y_i = knots[i]
                x_im1, y_im1 = knots[i - 1]
                for x in linspace(x_im1, x_i):
                    for y in linspace(y_im1, y_i):
                        grid[(x, y)] = "#"
    return grid


# For debugging
def draw(grid):
    x_min = min(x for x, _ in grid)
    x_max = max(x for x, _ in grid)
    y_max = max(y for _, y in grid)
    s = ""
    for y in range(y_max + 1):
        for x in range(x_min, x_max + 1):
            s += grid[(x, y)] if (x, y) in grid else "."
        s += "\n"
    print(s)


def drop(grid, y_max=2 ** 63):
    x, y = SOURCE
    while True:
        if y > y_max:
            return False
        if (x, y + 1) not in grid:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in grid:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in grid:
            x, y = x + 1, y + 1
        else:
            grid[(x, y)] = "o"
            return True


def capacity(grid):
    y_max = max(y for _, y in grid)
    for i in range(2 ** 63):
        if not drop(grid, y_max):
            return i


if __name__ == "__main__":
    grid = read_grid("input.txt")
    print(capacity(grid))
