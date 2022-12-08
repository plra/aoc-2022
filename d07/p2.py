from p1 import size_dirs

TOTAL_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000

if __name__ == "__main__":
    dir_sizes = size_dirs("input.txt")
    extra_space_needed = REQUIRED_FREE_SPACE - (TOTAL_SPACE - dir_sizes["/"])
    print(min(size for size in dir_sizes.values() if size >= extra_space_needed))
