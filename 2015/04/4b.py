# API stuff

from aocd import get_data, submit
part = "a" if "a" in __file__.split("/")[-1] else "b"
day, year = int(__file__.split("/")[-2]), int(__file__.split("/")[-3])
data = get_data(day=day, year=year)

# solution

from hashlib import md5

counter = 0

while True:
    counter += 1
    if md5(f"{data}{counter}".encode()).hexdigest()[:6] == "000000":
        answer = counter
        break

# submission

submit(answer, part=part, day=day, year=year)
