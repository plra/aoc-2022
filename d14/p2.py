from p1 import SOURCE, read_grid, drop


# Dumb manual floor width parameter
def add_floor(grid, buffer):
    y_max = max(y for _, y in grid)
    x_min = min(x for x, _ in grid)
    x_max = max(x for x, _ in grid)

    for x in range(x_min - buffer, x_max + buffer):
        grid[(x, y_max + 2)] = "#"


def capacity(grid):
    for i in range(2 ** 63):
        if grid[SOURCE] == "o":
            return i
        drop(grid)


if __name__ == "__main__":
    grid = read_grid("input.txt")
    add_floor(grid, 1000)
    print(capacity(grid))
