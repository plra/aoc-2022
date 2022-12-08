import re
from os.path import normpath, join


def size_dirs(input_filename):
    dir_sizes = {}
    with open(input_filename) as f:
        cwd = ""
        for line in f:
            line = line.strip()
            # Only cd calls and file (not subdirectory) listings are needed to build filetree
            if line.startswith("$ cd "):
                dest = line.split()[-1]
                # Handles "/" and ".." cases
                cwd = normpath(join(cwd, dest))
                if cwd not in dir_sizes:
                    dir_sizes[cwd] = 0
            elif re.match(r"^\d+ .*", line):
                size = int(line.split()[0])
                for dir in dir_sizes.keys():
                    if cwd.startswith(dir):  # Includes dir == cwd
                        dir_sizes[dir] += size
    return dir_sizes


if __name__ == "__main__":
    dir_sizes = size_dirs("input.txt")
    print(sum(size for size in dir_sizes.values() if size <= 10 ** 5))
