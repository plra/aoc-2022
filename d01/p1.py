import itertools

print(
    max(
        sum(map(int, items))
        for nonempty, items in itertools.groupby(
            open("input.txt").readlines(), lambda s: s != "\n"
        )
        if nonempty
    )
)
