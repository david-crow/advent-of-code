# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import hashlib

answer = ""
idx = 0

while len(answer) < 8:
    idx += 1
    hash = hashlib.md5((data + str(idx)).encode()).hexdigest()

    if hash[:5] == "00000":
        answer += hash[5]

# submission

submit(answer, part=part, day=day, year=year)
