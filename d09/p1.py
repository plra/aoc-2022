def read_directions(filename):
    with open(filename) as f:
        return [(line[0], int(line[2:])) for line in f]


def sign(x):
    return 0 if x == 0 else (-1) ** (x < 0)


def move_head(head_pos, dir):
    head_x, head_y = head_pos
    if dir == "R":
        return (head_x + 1, head_y)
    elif dir == "U":
        return (head_x, head_y + 1)
    elif dir == "L":
        return (head_x - 1, head_y)
    elif dir == "D":
        return (head_x, head_y - 1)


# Get new tail_pos given new head_pos. Assumes previous position was valid.
def follow(head_pos, tail_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos
    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:  # Not adjacent
        # Move x- and y-coords 1 closer to head. This covers all cases.
        tail_x += sign(head_x - tail_x)
        tail_y += sign(head_y - tail_y)
    return (tail_x, tail_y)


def get_tail_positions(directions):
    head_pos = tail_pos = (0, 0)
    tail_positions = {tail_pos}
    for dir, n in directions:
        for _ in range(n):
            head_pos = move_head(head_pos, dir)
            tail_pos = follow(head_pos, tail_pos)
            tail_positions.add(tail_pos)
    return tail_positions


if __name__ == "__main__":
    directions = read_directions("input.txt")
    tail_positions = get_tail_positions(directions)
    print(len(tail_positions))
