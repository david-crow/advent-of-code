# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

data = [d.split(",") for d in data.split("\n")]
data = [(list(map(int, a.split("-"))), list(map(int, b.split("-")))) for a, b in data]

def encompasses(a, b):
    return (a[0] <= b[0] and b[1] <= a[1]) or (b[0] <= a[0] and a[1] <= b[1])

answer = sum([encompasses(a, b) for a, b in data])

# submission

submit(answer, part=part, day=day, year=year)
