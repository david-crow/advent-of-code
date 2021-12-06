# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

dims = [list(map(int, d.split("x"))) for d in data.split()]
answer = 0

for d in dims:
    l, w, h = sorted(d)
    areas = [l * w, l * h, w * h]
    answer += 2 * sum(areas) + min(areas)

# submission

submit(answer, part=part, day=day, year=year)
