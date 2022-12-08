def read_grid(filename):
    with open(filename) as f:
        return [[int(d) for d in line.strip()] for line in f.readlines()]


def is_visible(grid, r, c):
    height = grid[r][c]
    # Search from above, below, left, then right
    return (
        all(grid[i][c] < height for i in range(r))
        or all(grid[i][c] < height for i in range(r + 1, len(grid)))
        or all(grid[r][j] < height for j in range(c))
        or all(grid[r][j] < height for j in range(c + 1, len(grid[0])))
    )


if __name__ == "__main__":
    grid = read_grid("input.txt")
    n_visible = sum(
        is_visible(grid, r, c) for r in range(len(grid)) for c in range(len(grid[0]))
    )
    print(n_visible)
