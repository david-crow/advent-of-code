# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = sorted([sum(map(int, d.split("\n"))) for d in data.split("\n\n")], reverse=True)

# submission

answer = sum(data[:3])
submit(answer, part=part, day=day, year=year)
