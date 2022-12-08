from p1 import read_grid


def n_visible(height, line_of_sight_heights):
    n = 0
    for h in line_of_sight_heights:
        n += 1
        if h >= height:
            break
    return n


def scenic_score(grid, r, c):
    height = grid[r][c]
    up_score = n_visible(height, [grid[i][c] for i in reversed(range(r))])
    down_score = n_visible(height, [grid[i][c] for i in range(r + 1, len(grid))])
    left_score = n_visible(height, [grid[r][j] for j in reversed(range(c))])
    right_score = n_visible(height, [grid[r][j] for j in range(c + 1, len(grid[0]))])
    return up_score * down_score * left_score * right_score


if __name__ == "__main__":
    grid = read_grid("input.txt")
    print(
        max(
            scenic_score(grid, r, c)
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )
    )
