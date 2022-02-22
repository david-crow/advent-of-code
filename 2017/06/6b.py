# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [int(d) for d in data.split()]
banks, lim = [], len(data)

while data not in banks:
    banks.append(data.copy())
    idx = data.index(max(data))
    val = data[idx]
    data[idx] = 0

    for _ in range(val):
        idx = idx + 1 if idx + 1 < lim else 0
        data[idx] += 1

answer = len(banks) - banks.index(data)

# submission

submit(answer, part=part, day=day, year=year)
