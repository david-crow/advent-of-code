# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from collections import defaultdict, Counter

counts = defaultdict(list)
answer = 0

data = [d.split("-") for d in data.split("\n")]
data = [("".join(d[:-1]), d[-1][:-7], d[-1][-6:-1]) for d in data]

for d in data:
    counted = Counter(d[0]).most_common()
    checksum = "".join([k for k, v in sorted(counted, key=lambda x: (-x[1], x[0]))[:5]])
    answer += int(d[1]) * (checksum == d[2])

# submission

# print(answer)
submit(answer, part=part, day=day, year=year)
