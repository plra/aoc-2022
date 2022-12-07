import re

INSTR_REGEX = r"move (\d+) from (\d+) to (\d+)"


def read_input(filename):
    with open(filename) as f:
        # Process initial crate stacks. First get rows, then transpose.
        rows = []
        n_stacks = None
        for crate_line in f:
            if crate_line[1] == "1":
                # We're at index line, e.g. " 1   2   3 ". Extract number of stacks and proceed.
                n_stacks = int(crate_line.split()[-1])
                f.readline()  # Skip newline
                break
            # Crate labels are at positions 1, 5, 9, ...
            rows.append(list(crate_line[1 : len(crate_line) : 4]))
        # "Build" stacks from bottom row up
        stacks = [[] for _ in range(n_stacks)]
        for row in reversed(rows):
            for i in range(len(row)):
                if row[i] != " ":
                    stacks[i].append(row[i])

        # Process move instructions
        instrs = []
        for instr_line in f:
            # Each instr line is "move n from i+1 to j+1". We record instrs as (n, i, j)
            n, i_plus_1, j_plus_1 = map(
                int, re.match(INSTR_REGEX, instr_line).group(1, 2, 3)
            )
            instrs.append((n, i_plus_1 - 1, j_plus_1 - 1))

        return stacks, instrs


if __name__ == "__main__":
    stacks, instrs = read_input("input.txt")
    for n, i, j in instrs:
        # Move crates one by one
        for _ in range(n):
            stacks[j].append(stacks[i].pop())
    message = "".join(stack[-1] for stack in stacks if stack)
    print(message)
