# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

# "The On-Line Encyclopedia of Integer Sequences" already has this sequence, soo...
# https://oeis.org/A141481

import requests

nums = requests.get("https://oeis.org/A141481/b141481.txt").text
nums = {n.split(" ")[0] : int(n.split(" ")[1]) for n in nums.splitlines()[2:-7]}
nums = [v for v in nums.values() if v >= int(data)]

answer = min(nums)

# submission

submit(answer, part=part, day=day, year=year)
