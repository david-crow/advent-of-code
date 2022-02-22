# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [int(d) for d in data.split("\n")]
idx, idx_range = 0, range(len(data))
answer = 0

while idx in idx_range:
    answer += 1
    tmp = data[idx]
    data[idx] += 1 if tmp < 3 else -1
    idx += tmp

# submission

submit(answer, part=part, day=day, year=year)
