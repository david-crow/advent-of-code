# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split() for d in data.split("\n")]
data = [(d[0], int(d[3]), int(d[6]), int(d[13])) for d in data]

distances = {}
limit = 2503

for d in data:
    step, distance = 0, 0
    v, t0, t1 = d[1], d[2], d[3]

    while step + t0 + t1 < limit:
        distance += v * t0
        step += t0 + t1
    
    distances[d[0]] = distance + d[1] * min(t0, limit - step)

answer = max(distances.values())

# submission

print(answer)
submit(answer, part=part, day=day, year=year)
