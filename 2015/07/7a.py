# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

calc = {}
results = {}

for command in data.split("\n"):
    (ops, res) = command.split(" -> ")
    calc[res] = ops.split()

def evaluate(key):
    try:
        return int(key)
    except ValueError:
        pass

    if key not in results:
        ops = calc[key]

        if len(ops) == 1:
            res = evaluate(ops[0])

        else:
            op = ops[-2]

            if op == "AND":
                res = evaluate(ops[0]) & evaluate(ops[2])
            elif op == "OR":
                res = evaluate(ops[0]) | evaluate(ops[2])
            elif op == "NOT":
                res = ~evaluate(ops[1]) & 0xffff
            elif op == "LSHIFT":
                res = evaluate(ops[0]) << evaluate(ops[2])
            elif op == "RSHIFT":
                res = evaluate(ops[0]) >> evaluate(ops[2])

        results[key] = res

    return results[key]

answer = evaluate("a")

# submission

submit(answer, part=part, day=day, year=year)
