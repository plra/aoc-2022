import re
from p1 import read_input


if __name__ == "__main__":
    stacks, instrs = read_input("input.txt")
    for n, i, j in instrs:
        # Move n crates at once
        stacks[j].extend(stacks[i][-n:])
        stacks[i] = stacks[i][:-n]
    message = "".join(stack[-1] for stack in stacks if stack)
    print(message)
