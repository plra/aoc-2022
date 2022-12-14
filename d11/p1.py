def read_input(filename):
    with open(filename) as f:
        monkeys = []
        for line in f:
            if not line.strip():
                continue
            monkey = {}
            monkey["ws"] = [int(w) for w in f.readline()[18:].split(", ")]
            operator, operand = f.readline()[23:].split()
            if operand == "old":
                monkey["update_fn"] = lambda old: old ** 2
            elif operator == "*":
                monkey["update_fn"] = lambda old, op=int(operand): old * op
            elif operator == "+":
                monkey["update_fn"] = lambda old, op=int(operand): old + op
            monkey["modulus"] = int(f.readline()[21:])
            true_target = int(f.readline()[29:])
            false_target = int(f.readline()[30:])
            monkey["targets"] = (false_target, true_target)
            monkey["n_inspections"] = 0
            monkeys.append(monkey)
        return monkeys


def run_round(monkeys):
    for monkey in monkeys:
        for w in monkey["ws"]:
            w_new = monkey["update_fn"](w) // 3
            test_result = w_new % monkey["modulus"] == 0
            target_index = monkey["targets"][test_result]
            monkeys[target_index]["ws"].append(w_new)
            monkey["n_inspections"] += 1
        monkey["ws"].clear()
    return monkeys


def monkey_business(monkeys):
    return int.__mul__(*sorted([monkey["n_inspections"] for monkey in monkeys])[-2:])


if __name__ == "__main__":
    monkeys = read_input("input.txt")
    for _ in range(20):
        run_round(monkeys)
    print(monkey_business(monkeys))
