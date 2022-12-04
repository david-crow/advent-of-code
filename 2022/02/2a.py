# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

matches = {"X": "A", "Y": "B", "Z": "C"}
wins = {"A": "B", "B": "C", "C": "A"}
scores = {"A" : 1, "B" : 2, "C" : 3}

for k, v in matches.items():
    data = data.replace(k, v)

data = [d.split() for d in data.split("\n")]
answer = 0

for (c, p) in data:
    answer += scores[p]

    if c == p:
        answer += 3
    elif p == wins[c]:
        answer += 6

# submission

submit(answer, part=part, day=day, year=year)
