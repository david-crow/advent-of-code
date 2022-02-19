# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

import hashlib

answer = ["-"] * 8
nums = "1234567890"
idx = -1

while "-" in answer:
    idx += 1
    hash = hashlib.md5((data + str(idx)).encode()).hexdigest()

    if hash[:5] == "00000" and hash[5] in nums:
        pos = int(hash[5])

        if pos in list(range(0, 8)) and answer[pos] == "-":
            answer[pos] = hash[6]

# submission

submit(answer, part=part, day=day, year=year)
