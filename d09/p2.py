from p1 import read_directions, move_head, follow


def get_tail_positions(directions, n_knots):
    knot_positions = [(0, 0) for _ in range(n_knots)]  # [head_pos, ..., tail_pos]
    tail_positions = {knot_positions[-1]}
    for dir, n in directions:
        for _ in range(n):
            # Move head then update knot positions sequentially
            knot_positions[0] = move_head(knot_positions[0], dir)
            for i in range(1, n_knots):
                knot_positions[i] = follow(knot_positions[i - 1], knot_positions[i])
            tail_positions.add(knot_positions[-1])
    return tail_positions


if __name__ == "__main__":
    directions = read_directions("input.txt")
    tail_positions = get_tail_positions(directions, 10)
    print(len(tail_positions))
