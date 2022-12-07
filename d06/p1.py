# 1-indexed
def index_of_first_heterogeneous_substring(s, n):
    for i in range(n, len(s)):
        if len(set(s[i - n : i])) == n:
            # n characters s[i-n], ..., s[i-1] are distinct
            return i


if __name__ == "__main__":
    with open("input.txt") as f:
        print(index_of_first_heterogeneous_substring(f.readline(), 4))
