# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [[int(y) for y in x] for x in data.split("\n")]
xmax, ymax = len(data[0]), len(data)
big_data = [[0 for _ in range(5 * xmax)] for _ in range(5 * ymax)]

def valid(v):
    return v[0] in range(len(data)) and v[1] in range(len(data[0]))

def neighbors(v):
    x, y = v[0], v[1]
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

for x in range(len(big_data[0])):
    for y in range(len(big_data)):
        dist = x // xmax + y // ymax
        newval = data[y % ymax][x % xmax]

        for i in range(dist):
            newval = newval + 1 if newval < 9 else 1

        big_data[x][y] = newval

data = big_data
q = [(0, 0, 0)]
costs = {}

while True:
    cost, x, y = q[0]
    q = q[1:]

    if x == len(data) - 1 and y == len(data[0]) - 1: 
        answer = cost
        break

    for n in neighbors((x, y)):
        if valid((n[0], n[1])):
            alternate = cost + data[n[0]][n[1]]

            if (n[0], n[1]) not in costs or costs[(n[0], n[1])] > alternate:
                costs[(n[0], n[1])] = alternate
                q.append((alternate, n[0], n[1]))

    q = sorted(q)

# submission

submit(answer, part=part, day=day, year=year)
