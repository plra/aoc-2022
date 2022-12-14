from p1 import read_input, monkey_business


# This time track worry values modulo all monkeys' moduli in a list of length
# n_monkeys rather than maintaining a single int (which will overflow).
def add_residues(monkeys):
    for monkey in monkeys:
        monkey["residue_sets"] = []
        for w in monkey["ws"]:
            residue_set = [w % monkey["modulus"] for monkey in monkeys]
            monkey["residue_sets"].append(residue_set)
    return monkeys


def run_round(monkeys):
    for i, monkey in enumerate(monkeys):
        for residue_set in monkey["residue_sets"]:
            # Compute new worry value mod current monkey's modulus to determine
            # target monkey index
            residue_new = monkey["update_fn"](residue_set[i]) % monkey["modulus"]
            target_index = monkey["targets"][residue_new == 0]
            # Compute new worry values mod all monkeys' moduli
            monkeys[target_index]["residue_sets"].append(
                [
                    monkey["update_fn"](residue) % monkeys[j]["modulus"]
                    for j, residue in enumerate(residue_set)
                ]
            )
            monkey["n_inspections"] += 1
        monkey["residue_sets"].clear()
    return monkeys


if __name__ == "__main__":
    monkeys = read_input("input.txt")
    add_residues(monkeys)
    for _ in range(10000):
        run_round(monkeys)
    print(monkey_business(monkeys))
