# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from functools import reduce

def add_left(n, x):
    if x is None:
        return n

    if isinstance(n, int):
        return n + x

    return [add_left(n[0], x), n[1]]

def add_right(n, x):
    if x is None:
        return n

    if isinstance(n, int):
        return n + x

    return [n[0], add_right(n[1], x)]

def explode(n, d=4):
    if isinstance(n, int):
        return False, None, n, None

    if d == 0:
        return True, n[0], 0, n[1]

    a, b = n
    exploded, left, a, right = explode(a, d - 1)

    if exploded:
        return True, left, [a, add_left(b, right)], None

    exploded, left, b, right = explode(b, d - 1)

    if exploded:
        return True, None, [add_right(a, left), b], right

    return False, None, n, None

def split(n):
    if isinstance(n, int):
        if n >= 10:
            return True, [n // 2, (n + 1) // 2]

        return False, n

    a, b = n
    changed, a = split(a)

    if changed:
        return True, [a, b]

    changed, b = split(b)
    return changed, [a, b]

def add(a, b):
    n = [a, b]

    while True:
        changed, _, n, _ = explode(n)

        if not changed:
            changed, n = split(n)

        if not changed:
            break

    return n

def magnitude(n):
    if isinstance(n, int):
        return n

    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

data = [eval(d) for d in data.split("\n")]
answer = magnitude(reduce(add, data))

# submission

submit(answer, part=part, day=day, year=year)
