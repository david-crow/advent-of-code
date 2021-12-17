# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from itertools import permutations

pairs = {}
guests = set()

for line in data.split("\n"):
    line = line.split()
    guests |= {line[0]}
    pairs[(line[0], line[-1][:-1])] = int(line[3]) if line[2] == "gain" else -int(line[3])

answer = 0

for g in guests:
    pairs[(g, "DC")] = 0
    pairs[("DC", g)] = 0

guests |= {"DC"}

for perm in list(permutations(guests)):
    neighbors = [(perm[0], perm[-1])] + [(perm[i], perm[i + 1]) for i in range(len(perm) - 1)]
    val = sum(pairs[n] + pairs[n[::-1]] for n in neighbors)
    answer = max(answer, val)

# submission

submit(answer, part=part, day=day, year=year)
