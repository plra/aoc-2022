from p1 import index_of_first_heterogeneous_substring

if __name__ == "__main__":
    with open("input.txt") as f:
        print(index_of_first_heterogeneous_substring(f.readline(), 14))
